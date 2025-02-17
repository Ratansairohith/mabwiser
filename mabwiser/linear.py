# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0

from copy import deepcopy
from typing import Callable, Dict, List, NoReturn, Optional, Union

import numpy as np
from sklearn.preprocessing import StandardScaler

from mabwiser.base_mab import BaseMAB
from mabwiser.utils import Arm, Num, argmax, _BaseRNG, create_rng

SCALER_TOLERANCE = 1e-6


def fix_small_variance(scaler: StandardScaler) -> NoReturn:
    """
    Set variances close to zero to be equal to one in trained standard scaler to make computations stable.

    :param scaler: the scaler to check and fix variances for
    """
    if hasattr(scaler, 'scale_') and hasattr(scaler, 'var_'):
        # Get a mask to pull indices where std smaller than scaler_tolerance
        mask = scaler.scale_ <= SCALER_TOLERANCE

        # Fix standard deviation
        scaler.scale_[mask] = 1.0e+00

        # Fix variance accordingly. var_ is allowed to be 0 in scaler.
        # This helps to track if scale_ are set as ones due to zeros in variances.
        scaler.var_[mask] = 0.0e+00


class _RidgeRegression:

    def __init__(self, rng: _BaseRNG, alpha: Num = 1.0, l2_lambda: Num = 1.0, scale: bool = False):

        # Ridge Regression: https://onlinecourses.science.psu.edu/stat857/node/155/
        self.rng = rng                      # random number generator
        self.alpha = alpha                  # exploration parameter
        self.l2_lambda = l2_lambda          # regularization parameter
        self.scale = scale                  # scale contexts

        self.beta = None                    # (XtX + l2_lambda * I_d)^-1 * Xty = A^-1 * Xty
        self.A = None                       # (XtX + l2_lambda * I_d)
        self.A_inv = None                   # (XtX + l2_lambda * I_d)^-1
        self.Xty = None
        self.scaler = None

    def init(self, num_features):
        # By default, assume that
        # A is the identity matrix and Xty is set to 0
        self.Xty = np.zeros(num_features)
        self.A = self.l2_lambda * np.identity(num_features)
        self.A_inv = self.A.copy()
        self.beta = np.dot(self.A_inv, self.Xty)
        self.scaler = StandardScaler() if self.scale else None

    def fit(self, X, y):

        # Scale
        if self.scaler is not None:
            X = X.astype('float64')
            if not hasattr(self.scaler, 'scale_'):
                self.scaler.fit(X)
            else:
                self.scaler.partial_fit(X)
            fix_small_variance(self.scaler)
            X = self.scaler.transform(X)

        # X transpose
        Xt = X.T

        # Update A
        self.A = self.A + np.dot(Xt, X)
        self.A_inv = np.linalg.inv(self.A)

        # Add new Xty values to old
        self.Xty = self.Xty + np.dot(Xt, y)

        # Recalculate beta coefficients
        self.beta = np.dot(self.A_inv, self.Xty)

    def predict(self, x):

        # Scale
        if self.scaler is not None:
            x = self._scale_predict_context(x)

        # Calculate default expectation y = x * b
        return np.dot(x, self.beta)

    def _scale_predict_context(self, x):
        if not hasattr(self.scaler, 'scale_'):
            return x

        # Reshape 1D array to 2D
        x = x.reshape(1, -1)

        # Transform and return to previous shape. Convert to float64 to suppress any type warnings.
        return self.scaler.transform(x.astype('float64')).reshape(-1)


class _LinTS(_RidgeRegression):

    def predict(self, x):

        # Scale
        if self.scaler is not None:
            x = self._scale_predict_context(x)

        # Randomly sample coefficients from multivariate normal distribution
        # Covariance is enhanced with the exploration factor
        beta_sampled = self.rng.multivariate_normal(self.beta, np.square(self.alpha) * self.A_inv)

        # Calculate expectation y = x * beta_sampled
        return np.dot(x, beta_sampled)


class _LinUCB(_RidgeRegression):

    def predict(self, x):

        # Scale
        if self.scaler is not None:
            x = self._scale_predict_context(x)

        # Upper confidence bound = alpha * sqrt(x A^-1 xt). Notice that, x = xt
        ucb = (self.alpha * np.sqrt(np.dot(np.dot(x, self.A_inv), x)))

        # Calculate linucb expectation y = x * b + ucb
        return np.dot(x, self.beta) + ucb


class _Linear(BaseMAB):

    factory = {"ts": _LinTS, "ucb": _LinUCB, "ridge": _RidgeRegression}

    def __init__(self, rng: _BaseRNG, arms: List[Arm], n_jobs: int, backend: Optional[str],
                 alpha: Num, epsilon: Num, l2_lambda: Num, regression: str, scale: bool):
        super().__init__(rng, arms, n_jobs, backend)
        self.alpha = alpha
        self.epsilon = epsilon
        self.l2_lambda = l2_lambda
        self.regression = regression
        self.scale = scale
        self.num_features = None

        # Create regression model for each arm
        self.arm_to_model = dict((arm, _Linear.factory.get(regression)(rng, alpha, l2_lambda, scale)) for arm in arms)

    def fit(self, decisions: np.ndarray, rewards: np.ndarray, contexts: np.ndarray = None) -> NoReturn:

        # Initialize each model by arm
        self.num_features = contexts.shape[1]
        for arm in self.arms:
            self.arm_to_model[arm].init(num_features=self.num_features)

        # Reset warm started arms
        self.cold_arm_to_warm_arm = dict()

        # Perform parallel fit
        self._parallel_fit(decisions, rewards, contexts)

    def partial_fit(self, decisions: np.ndarray, rewards: np.ndarray, contexts: np.ndarray = None) -> NoReturn:
        # Perform parallel fit
        self._parallel_fit(decisions, rewards, contexts)

    def predict(self, contexts: np.ndarray = None) -> Union[Arm, List[Arm]]:
        # Return predict for the given context
        return self._parallel_predict(contexts, is_predict=True)

    def predict_expectations(self, contexts: np.ndarray = None) -> Union[Dict[Arm, Num], List[Dict[Arm, Num]]]:
        # Return predict expectations for the given context
        return self._parallel_predict(contexts, is_predict=False)

    def _copy_arms(self, cold_arm_to_warm_arm):
        for cold_arm, warm_arm in cold_arm_to_warm_arm.items():
            self.arm_to_model[cold_arm] = deepcopy(self.arm_to_model[warm_arm])

    def _uptake_new_arm(self, arm: Arm, binarizer: Callable = None):

        # Add to untrained_arms arms
        self.arm_to_model[arm] = _Linear.factory.get(self.regression)(self.rng, self.alpha, self.l2_lambda, self.scale)

        # If fit happened, initialize the new arm to defaults
        is_fitted = self.num_features is not None
        if is_fitted:
            self.arm_to_model[arm].init(num_features=self.num_features)

    def _fit_arm(self, arm: Arm, decisions: np.ndarray, rewards: np.ndarray, contexts: Optional[np.ndarray] = None):

        # Get local copy of model to minimize communication overhead
        # between arms (processes) using shared object
        lr = deepcopy(self.arm_to_model[arm])

        # Skip the arms with no data
        indices = np.where(decisions == arm)
        if indices[0].size == 0:
            return lr

        # Fit the regression
        X = contexts[indices]
        y = rewards[indices]
        lr.fit(X, y)

        self.arm_to_model[arm] = lr

    def _predict_contexts(self, contexts: np.ndarray, is_predict: bool,
                          seeds: Optional[np.ndarray] = None, start_index: Optional[int] = None) -> List:

        # Get local copy of model, arm_to_expectation and arms to minimize
        # communication overhead between arms (processes) using shared objects
        arm_to_model = deepcopy(self.arm_to_model)
        arm_to_expectation = deepcopy(self.arm_to_expectation)
        arms = deepcopy(self.arms)

        # Create an empty list of predictions
        predictions = [None] * len(contexts)
        for index, row in enumerate(contexts):
            # Each row needs a separately seeded rng for reproducibility in parallel
            rng = create_rng(seed=seeds[index])

            # With epsilon probability set arm expectation to random value
            if rng.rand() < self.epsilon:
                for arm in arms:
                    arm_to_expectation[arm] = rng.rand()

            else:
                # Create new seeded generator for model to ensure reproducibility
                model_rng = create_rng(seed=seeds[index])
                for arm in arms:
                    arm_to_model[arm].rng = model_rng

                    # Get the expectation of each arm from its trained model
                    arm_to_expectation[arm] = arm_to_model[arm].predict(row)

            if is_predict:
                predictions[index] = argmax(arm_to_expectation)
            else:
                predictions[index] = arm_to_expectation.copy()

        # Return list of predictions
        return predictions

    def _drop_existing_arm(self, arm: Arm) -> NoReturn:
        self.arm_to_model.pop(arm)
