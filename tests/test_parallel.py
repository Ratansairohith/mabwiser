# -*- coding: utf-8 -*-

import numpy as np

from mabwiser.mab import LearningPolicy, NeighborhoodPolicy
from tests.test_base import BaseTest


class ParallelTest(BaseTest):

    def test_greedy_t1(self):

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertEqual(arms, [1, 1, 1, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertEqual(arms, [1, 1, 1, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=3)

        self.assertEqual(arms, [1, 1, 1, 1])

    def test_popularity(self):

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.Popularity(),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertEqual(arms, [3, 2, 3, 3])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.Popularity(),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertEqual(arms, [3, 2, 3, 3])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.Popularity(),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=3)

        self.assertEqual(arms, [3, 2, 3, 3])

    def test_greedy_t2(self):

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0.25),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertEqual(arms, [1, 1, 1, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0.25),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertEqual(arms, [1, 1, 1, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0.25),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=3)

        self.assertEqual(arms, [1, 1, 1, 1])

    def test_greedy_t3(self):

        arms, mab = self.predict(arms=[1, 2, 3, 4],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0.9),
                                 seed=123456,
                                 num_run=6,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertEqual(arms, [3, 3, 3, 1, 2, 3])

        arms, mab = self.predict(arms=[1, 2, 3, 4],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0.9),
                                 seed=123456,
                                 num_run=6,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertEqual(arms, [3, 3, 3, 1, 2, 3])

        arms, mab = self.predict(arms=[1, 2, 3, 4],
                                 decisions=[1, 1, 1, 3, 2, 2, 3, 1, 3],
                                 rewards=[0, 1, 1, 0, 1, 0, 1, 1, 1],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=0.9),
                                 seed=123456,
                                 num_run=6,
                                 is_predict=True,
                                 n_jobs=4)

        self.assertEqual(arms, [3, 3, 3, 1, 2, 3])

    def test_UCB1_t1(self):

        arms, mab = self.predict(arms=[1, 2, 3, 4],
                                 decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                 rewards=[1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                                 learning_policy=LearningPolicy.UCB1(alpha=0.1),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertEqual(arms, [2, 2, 2, 2])

        arms, mab = self.predict(arms=[1, 2, 3, 4],
                                 decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                 rewards=[1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                                 learning_policy=LearningPolicy.UCB1(alpha=0.1),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertEqual(arms, [2, 2, 2, 2])

        arms, mab = self.predict(arms=[1, 2, 3, 4],
                                 decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                 rewards=[1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
                                 learning_policy=LearningPolicy.UCB1(alpha=0.1),
                                 seed=123456,
                                 num_run=4,
                                 is_predict=True,
                                 n_jobs=4)

        self.assertEqual(arms, [2, 2, 2, 2])

    def test_thompson_t1(self):

        arms, mab = self.predict(arms=[1, 2, 3, 4],
                                 decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                 rewards=[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 seed=123456,
                                 num_run=8,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertEqual(arms, [3, 3, 3, 3, 4, 4, 4, 3])

        arms, mab = self.predict(arms=[1, 2, 3, 4],
                                 decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                 rewards=[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 seed=123456,
                                 num_run=8,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertEqual(arms, [3, 3, 3, 3, 4, 4, 4, 3])

        arms, mab = self.predict(arms=[1, 2, 3, 4],
                                 decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                 rewards=[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 seed=123456,
                                 num_run=8,
                                 is_predict=True,
                                 n_jobs=-1)

        self.assertEqual(arms, [3, 3, 3, 3, 4, 4, 4, 3])

    def test_UCB1_c2(self):

        rng = np.random.RandomState(seed=111)
        contexts_history = rng.randint(0, 5, (10, 5))
        contexts = rng.randint(0, 5, (10, 5))

        arm, mab = self.predict(arms=[1, 2, 3, 4],
                                decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                rewards=[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                                learning_policy=LearningPolicy.UCB1(alpha=0.1),
                                neighborhood_policy=NeighborhoodPolicy.Clusters(2),
                                context_history=contexts_history,
                                contexts=contexts,
                                seed=123456,
                                num_run=5,
                                is_predict=True,
                                n_jobs=1)

        self.assertEqual(arm,  [[3, 3, 1, 1, 1, 1, 3, 1, 3, 3] for _ in range(5)])

        arm, mab = self.predict(arms=[1, 2, 3, 4],
                                decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                rewards=[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                                learning_policy=LearningPolicy.UCB1(alpha=0.1),
                                neighborhood_policy=NeighborhoodPolicy.Clusters(2),
                                context_history=contexts_history,
                                contexts=contexts,
                                seed=123456,
                                num_run=5,
                                is_predict=True,
                                n_jobs=2)

        self.assertEqual(arm,  [[3, 3, 1, 1, 1, 1, 3, 1, 3, 3] for _ in range(5)])

        arm, mab = self.predict(arms=[1, 2, 3, 4],
                                decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                rewards=[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                                learning_policy=LearningPolicy.UCB1(alpha=0.1),
                                neighborhood_policy=NeighborhoodPolicy.Clusters(2),
                                context_history=contexts_history,
                                contexts=contexts,
                                seed=123456,
                                num_run=5,
                                is_predict=True,
                                n_jobs=100)

        self.assertEqual(arm,  [[3, 3, 1, 1, 1, 1, 3, 1, 3, 3] for _ in range(5)])

    def test_greedy1_k2(self):
        rng = np.random.RandomState(seed=7)

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.KNearest(2),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertListEqual(arms, [2, 1, 1, 2, 3, 3, 3, 1, 3, 2])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.KNearest(2),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertListEqual(arms, [2, 1, 1, 2, 3, 3, 3, 1, 3, 2])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.KNearest(2),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=-1)

        self.assertListEqual(arms, [2, 1, 1, 2, 3, 3, 3, 1, 3, 2])

    def test_greedy1_r2(self):

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.Radius(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertListEqual(arms, [3, 1, 1, 3, 1, 3, 3, 1, 3, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.Radius(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertListEqual(arms, [3, 1, 1, 3, 1, 3, 3, 1, 3, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.Radius(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=-1)

        self.assertListEqual(arms, [3, 1, 1, 3, 1, 3, 3, 1, 3, 1])

    def test_greedy1_n3(self):
        rng = np.random.RandomState(seed=7)

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.Clusters(3),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertListEqual(arms, [2, 1, 1, 2, 3, 3, 3, 1, 3, 2])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.Clusters(3),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertListEqual(arms, [2, 1, 1, 2, 3, 3, 3, 1, 3, 2])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.Clusters(3),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=-1)

        self.assertListEqual(arms, [2, 1, 1, 2, 3, 3, 3, 1, 3, 2])

    def test_greedy1_a2(self):
        rng = np.random.RandomState(seed=7)

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.LSHNearest(),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertListEqual(arms, [1, 3, 3, 3, 1, 2, 1, 1, 2, 2])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.LSHNearest(),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertListEqual(arms, [1, 3, 3, 3, 1, 2, 1, 1, 2, 2])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.LSHNearest(),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=-1)

        self.assertListEqual(arms, [1, 3, 3, 3, 1, 2, 1, 1, 2, 2])

    def test_thompson_k2(self):

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.KNearest(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertListEqual(arms, [2, 1, 1, 2, 1, 1, 1, 2, 2, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.KNearest(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertListEqual(arms, [2, 1, 1, 2, 1, 1, 1, 2, 2, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.KNearest(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=-1)

        self.assertListEqual(arms, [2, 1, 1, 2, 1, 1, 1, 2, 2, 1])

    def test_thompson_r2(self):

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.Radius(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertListEqual(arms, [3, 1, 1, 3, 1, 3, 3, 1, 3, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.Radius(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertListEqual(arms, [3, 1, 1, 3, 1, 3, 3, 1, 3, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.Radius(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=-1)

        self.assertListEqual(arms, [3, 1, 1, 3, 1, 3, 3, 1, 3, 1])

    def test_thompson_n3(self):
        rng = np.random.RandomState(seed=7)

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.Clusters(3),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertListEqual(arms, [1, 2, 3, 3, 2, 1, 3, 1, 1, 3])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.Clusters(3),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertListEqual(arms, [3, 1, 1, 2, 1, 1, 1, 1, 1, 3])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.Clusters(3),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=-1)

        self.assertListEqual(arms, [3, 2, 3, 2, 2, 2, 3, 3, 2, 3])

    def test_thompson_a2(self):

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.LSHNearest(),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=1)

        self.assertListEqual(arms, [3, 1, 2, 2, 2, 3, 1, 2, 3, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.LSHNearest(),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2)

        self.assertListEqual(arms, [3, 1, 2, 2, 2, 3, 1, 2, 3, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.ThompsonSampling(),
                                 neighborhood_policy=NeighborhoodPolicy.LSHNearest(),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=-1)

        self.assertListEqual(arms, [3, 1, 2, 2, 2, 3, 1, 2, 3, 1])


    def test_linUCB(self):

        rng = np.random.RandomState(seed=111)
        contexts = rng.randint(0, 5, (10, 5))

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=1)

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 3])

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=2)

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 3])

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=-1)

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 3])

    def test_linUCB_expectations(self):

        rng = np.random.RandomState(seed=111)
        contexts = rng.randint(0, 5, (8, 5))
        expected_pred = [[1.1923304881612438,  0.386812974778054,   2.036795075137375],
                         [1.1383448695075555,  0.16604895162348998, 0.7454336659862624],
                         [0.39044990078495967, 0.32572728761335573, 1.0533787080477959],
                         [-0.9557496857893883, 0.4393900133310143,  1.4663248923093817],
                         [-0.4630963822269796, 0.44282983853389307, 1.4430098512988918],
                         [0.26667599463140623, 0.34807480426506293, 1.008245109800643],
                         [1.3255310649960248,  0.43761043197507354, 0.9787023941693738],
                         [0.33267910305673676, 0.29690114350965546, 1.460951676645638]]

        exps, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 1],
                                 rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                 learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                 context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                  [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                  [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                  [0, 2, 1, 0, 0]],
                                 contexts=contexts,
                                 seed=123456,
                                 num_run=1,
                                 is_predict=False,
                                 n_jobs=1)

        for i in range(len(expected_pred)):
            self.assertListAlmostEqual(exps[i].values(), expected_pred[i])

        exps, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 1],
                                 rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                 learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                 context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                  [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                  [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                  [0, 2, 1, 0, 0]],
                                 contexts=contexts,
                                 seed=123456,
                                 num_run=1,
                                 is_predict=False,
                                 n_jobs=2)

        for i in range(len(expected_pred)):
            self.assertListAlmostEqual(exps[i].values(), expected_pred[i])

        exps, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 1],
                                 rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                 learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                 context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                  [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                  [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                  [0, 2, 1, 0, 0]],
                                 contexts=contexts,
                                 seed=123456,
                                 num_run=1,
                                 is_predict=False,
                                 n_jobs=-1)

        for i in range(len(expected_pred)):
            self.assertListAlmostEqual(exps[i].values(), expected_pred[i])

    def test_linTS(self):

        rng = np.random.RandomState(seed=111)
        contexts = rng.randint(0, 5, (10, 5))

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinTS(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=1)

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 5])

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinTS(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=2)

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 5])

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinTS(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=-1)

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 5])

    def test_linTS_expectations(self):

        rng = np.random.RandomState(seed=111)
        contexts = rng.randint(0, 5, (5, 5))

        expected_pred = [[0.9167267352065508, 0.6800548963827412, 1.4147481760827891,
                          2.061680527026926, -0.6516833696912612],
                         [0.8104296620172513, 0.26691232761493117, 0.6503604017431508,
                          0.9977263420741849, -0.6447229745688157],
                         [-0.009581460000014294, 0.881059511216882, 1.0576520008395551,
                          0.4150322121520029, -0.26918983719229994],
                         [-0.38164469675190177, -0.3264960369736939, 1.3695993885284545,
                          0.55178010066725, 0.021790663220199458],
                         [-1.2613045626465647, -0.7305818793806982, 0.41438283892450944,
                          0.5208181269433911, -0.2673124934389858]]

        exps, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                 decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                 rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                 learning_policy=LearningPolicy.LinTS(alpha=0.1),
                                 context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                  [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                  [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                  [0, 2, 1, 0, 0]],
                                 contexts=contexts,
                                 seed=123456,
                                 num_run=1,
                                 is_predict=False,
                                 n_jobs=1)

        for i in range(len(expected_pred)):
            self.assertListAlmostEqual(exps[i].values(), expected_pred[i])

        exps, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                 decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                 rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                 learning_policy=LearningPolicy.LinTS(alpha=0.1),
                                 context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                  [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                  [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                  [0, 2, 1, 0, 0]],
                                 contexts=contexts,
                                 seed=123456,
                                 num_run=1,
                                 is_predict=False,
                                 n_jobs=2)

        for i in range(len(expected_pred)):
            self.assertListAlmostEqual(exps[i].values(), expected_pred[i])


        exps, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                 decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                 rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                 learning_policy=LearningPolicy.LinTS(alpha=0.1),
                                 context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                  [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                  [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                  [0, 2, 1, 0, 0]],
                                 contexts=contexts,
                                 seed=123456,
                                 num_run=1,
                                 is_predict=False,
                                 n_jobs=-1)

        for i in range(len(expected_pred)):
            self.assertListAlmostEqual(exps[i].values(), expected_pred[i])

    def test_UCB1_c2_backend(self):
        rng = np.random.RandomState(seed=111)
        contexts_history = rng.randint(0, 5, (10, 5))
        contexts = rng.randint(0, 5, (10, 5))

        arm, mab = self.predict(arms=[1, 2, 3, 4],
                                decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                rewards=[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                                learning_policy=LearningPolicy.UCB1(alpha=0.1),
                                neighborhood_policy=NeighborhoodPolicy.Clusters(2),
                                context_history=contexts_history,
                                contexts=contexts,
                                seed=123456,
                                num_run=5,
                                is_predict=True,
                                n_jobs=2,
                                backend=None)

        self.assertEqual(arm, [[3, 3, 1, 1, 1, 1, 3, 1, 3, 3] for _ in range(5)])

        arm, mab = self.predict(arms=[1, 2, 3, 4],
                                decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                rewards=[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                                learning_policy=LearningPolicy.UCB1(alpha=0.1),
                                neighborhood_policy=NeighborhoodPolicy.Clusters(2),
                                context_history=contexts_history,
                                contexts=contexts,
                                seed=123456,
                                num_run=5,
                                is_predict=True,
                                n_jobs=2,
                                backend='loky')

        self.assertEqual(arm, [[3, 3, 1, 1, 1, 1, 3, 1, 3, 3] for _ in range(5)])

        arm, mab = self.predict(arms=[1, 2, 3, 4],
                                decisions=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4],
                                rewards=[1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                                learning_policy=LearningPolicy.UCB1(alpha=0.1),
                                neighborhood_policy=NeighborhoodPolicy.Clusters(2),
                                context_history=contexts_history,
                                contexts=contexts,
                                seed=123456,
                                num_run=5,
                                is_predict=True,
                                n_jobs=2,
                                backend='threading')

        self.assertEqual(arm, [[3, 3, 1, 1, 1, 1, 3, 1, 3, 3] for _ in range(5)])

    def test_greedy1_k2_backend(self):
        rng = np.random.RandomState(seed=7)

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.KNearest(2),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2,
                                 backend=None)

        self.assertListEqual(arms, [2, 1, 1, 2, 3, 3, 3, 1, 3, 2])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.KNearest(2),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2,
                                 backend='loky')

        self.assertListEqual(arms, [2, 1, 1, 2, 3, 3, 3, 1, 3, 2])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.KNearest(2),
                                 context_history=[[rng.random_sample() for _ in range(5)] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2,
                                 backend='threading')

        self.assertListEqual(arms, [2, 1, 1, 2, 3, 3, 3, 1, 3, 2])

    def test_greedy1_r2_backend(self):
        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.Radius(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2,
                                 backend=None)

        self.assertListEqual(arms, [3, 1, 1, 3, 1, 3, 3, 1, 3, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.Radius(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2,
                                 backend='loky')

        self.assertListEqual(arms, [3, 1, 1, 3, 1, 3, 3, 1, 3, 1])

        arms, mab = self.predict(arms=[1, 2, 3],
                                 decisions=[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
                                 rewards=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                                 learning_policy=LearningPolicy.EpsilonGreedy(epsilon=1),
                                 neighborhood_policy=NeighborhoodPolicy.Radius(2),
                                 context_history=[[0, 0, 0, 0, 0] for _ in range(10)],
                                 contexts=[[1, 1, 1, 1, 1] for _ in range(10)],
                                 seed=123456,
                                 num_run=1,
                                 is_predict=True,
                                 n_jobs=2,
                                 backend='threading')

        self.assertListEqual(arms, [3, 1, 1, 3, 1, 3, 3, 1, 3, 1])

    def test_linUCB_backend(self):

        rng = np.random.RandomState(seed=111)
        contexts = rng.randint(0, 5, (10, 5))

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=1,
                                backend=None)

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 3])

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=2,
                                backend=None)

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 3])

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=2,
                                backend='loky')

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 3])

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinUCB(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=2,
                                backend='threading')

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 3])

    def test_linTS_backend(self):

        rng = np.random.RandomState(seed=111)
        contexts = rng.randint(0, 5, (10, 5))

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinTS(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=2,
                                backend=None)

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 5])

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinTS(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=2,
                                backend='loky')

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 5])

        arm, mab = self.predict(arms=[1, 2, 3, 4, 5],
                                decisions=[1, 1, 4, 2, 2, 2, 3, 3, 3, 1],
                                rewards=[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                                learning_policy=LearningPolicy.LinTS(alpha=0.1),
                                context_history=[[0, 1, 2, 3, 5], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0],
                                                 [0, 2, 2, 3, 5], [1, 3, 1, 1, 1], [0, 0, 0, 0, 0],
                                                 [0, 1, 4, 3, 5], [0, 1, 2, 4, 5], [1, 2, 1, 1, 3],
                                                 [0, 2, 1, 0, 0]],
                                contexts=contexts,
                                seed=123456,
                                num_run=1,
                                is_predict=True,
                                n_jobs=2,
                                backend='threading')

        self.assertEqual(arm, [4, 4, 3, 3, 4, 4, 4, 3, 4, 5])
