# __author__ = 'jonestj1'
#
# import mdtraj as md
# from mdtraj.testing import get_fn
#
# chain_lengths = [6, 8, 10, 12, 14, 16, 18]
# sqrt_nc = [4, 5, 6, 7, 8, 9, 10]
#
# traj = md.load('production_100_18.xtc', top=get_fn('production_100_18.top'))
# chain_indices = [[n+x for x in range(60)] for n in range(1800, 7800, 60)]
# print(chain_indices)
# S2 = md.compute_nematic_order(traj,indices='chain_indices')

import numpy as np

foo = np.zeros((7,7), dtype=np.int)
foo[0,0] = 7

print(foo)