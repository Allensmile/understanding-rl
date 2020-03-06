import argparse

import numpy as np
from car_rental import CarRentalEnv
from gridworld import Gridworld
from dynamic_programming import DynamicProgramming
from utils import print_transitions


def random_policy(env):
  def pi(s, a):
    return 1 / len(env.moves)
  return pi


def fig_4_1():
  env = Gridworld()
  pi_rand = random_policy(env)
  pi_init = {(a, s): pi_rand(s, a) for s in env.states for a in env.moves}
  alg = DynamicProgramming(env, pi=pi_init, theta=1e-4, gamma=1)  # undiscounted
  alg.policy_evaluation()
  alg.print_values()
  # show the optimal policy
  while not alg.policy_improvement(): pass
  alg.print_policy_gridworld()


def fig_4_2():
  env = CarRentalEnv()
  alg = DynamicProgramming(env, gamma=0.9, theta=1e-4)
  alg.policy_iteration(max_iter=1)
  alg.print_values()
  alg.print_policy_car_rental()


PLOT_FUNCTION = {
  '4.1': fig_4_1,
  '4.2': fig_4_2,
}


def main():
  parser = argparse.ArgumentParser()

  parser.add_argument('figure', type=str, default=None,
                      help='Figure to reproduce.',
                      choices=['4.1', '4.2'])
  args = parser.parse_args()

  PLOT_FUNCTION[args.figure]()


if __name__ == "__main__":
  main()
