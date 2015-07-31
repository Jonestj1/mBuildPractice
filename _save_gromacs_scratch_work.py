__author__ = 'jonestj1'

import mbuild as mb
from mbuild.compound import Compound
# # import foyer
# # import Intermol
# #

### Ethyl Benzene ###
class EtBen(mb.Compound):
    def __init__(self):
        super(EtBen, self).__init__()

        mb.load('/Users/jonestj1/ethylbenzene.pdb', compound=self)
        mb.translate(self, -self.atoms[0])

from mbuild.packing import *
from mbuild.box import Box
import numpy as np
ethylbenzene = EtBen()
# box_et_ben = fill_box(ethylbenzene, 100, [2, 2, 2])
# ethylbenzene.visualize()
traj = ethylbenzene.to_trajectory()
ethylbenzene.save_gromacs(filename='.gro', traj=traj)



# ### COe ###
# class PegMonomer(mb.Compound):
#     def __init__(self):
#         super(PegMonomer, self).__init__()
#
#         mb.load('peg_monomer.pdb', compound=self)
#         mb.translate(self, -self.C[0])
#
#         self.add(mb.Port(anchor=self.C[0]), 'down')
#         mb.translate(self.down, [0, -0.07, 0])
#
#
#         self.add(mb.Port(anchor=self.C[0]), 'up')
#         mb.translate(self.up, [0, 3.64, 0])
#
# peg_monomer = PegMonomer()
# peg_monomer.visualize()







# """Betacristobalite H backfill"""
# from mbuild.examples.alkane_monolayer.alkane_monolayer import AlkaneMonolayer
#
# mask = mb.grid_mask_2d(0, 0)
# betacristobalite = AlkaneMonolayer(mask)
# traj = betacristobalite.to_trajectory()
# betacristobalite.visualize()
# betacristobalite.save_gromacs('_betacristobalite', traj)

# """Brush"""
# from mbuild.examples.pmpc.brush import Brush
# brush = Brush()
# traj = brush.to_trajectory()
# brush.save_gromacs('_brush', traj)

# """Alkylsilane"""
# from mbuild.examples.alkane_monolayer.alkylsilane import AlkylSilane
# alkylsilane = AlkylSilane(chain_length=6)
# traj = alkylsilane.to_trajectory()
# alkylsilane.save_gromacs('_alkylsilane', traj, nr_excl=3)




# """ pMPC Brush Layer """
# from mbuild.examples.pmpc.pmpc_brush_layer import PMPCLayer
# mask = mb.grid_mask_2d(5, 5)
# pmpc_layer = PMPCLayer(mask,)
# pmpc_layer.visualize()
# traj = pmpc_layer.to_trajectory()
# pmpc_layer.save_gromacs(filename='pmpc_layer.gro', traj=traj)

# ### AlkaneMonolayer ###
# from mbuild.examples.alkane_monolayer.alkane_monolayer import AlkaneMonolayer
# mask = mb.grid_mask_2d(10, 10)
# # for x in range(6):
# #     for i in range(6):
# #         mask = mb.grid_mask_2d(x+5, x+5)
# alkane_monolayer = AlkaneMonolayer(chain_length=16+0*2, mask=mask,)
#         # alkane_monolayer.visualize()
# traj = alkane_monolayer.to_trajectory()
# alkane_monolayer.save_gromacs(filename='{0}_{1}_alkane_monolayer.gro'.format(0, 0),
#                                       traj=traj)
# for atom in alkane_monolayer.yield_atoms():
#     if atom.name != 'G':
#         print(atom.name)

# # alkane_monolayer.save_mol2('0_0_alkanemonolayer.mol2', traj)
# alkane_monolayer.visualize()

### Alkane Example ###
# from mbuild.examples.alkane.alkane import Alkane
# alkane = Alkane(n=10)
# alkane.save_gromacs(filename='alkane.gro', traj=alkane.to_trajectory())






# print(traj)

# for i, a in enumerate(traj.top._atoms):
#     print('atoms name={}, opls_type={}'.format(a.name, a.name))

# import mbuild as mb
# from foyer.atomtyper import find_atomtypes
from foyer.forcefield import prepare_atoms

# m = Methane()
# m = Ethane()
# m = mb.load(get_opls_fn('isopropane.pdb'))
# m = mb.load(get_opls_fn('cyclohexane.pdb'))
# m = mb.load(get_opls_fn('neopentane.pdb'))
# m = mb.load(get_opls_fn('benzene.pdb'))
# m = mb.load(get_opls_fn('1-propene.pdb'))
# m = mb.load(get_opls_fn('biphenyl.pdb'))

# traj = m.to_trajectory()
# prepare_atoms(traj.top)
# find_atomtypes(traj.top._atoms, forcefield='OPLS-AA')
#
# for i, a in enumerate(traj.top._atoms):
#     print("Atom name={}, opls_type={}".format(a.name, a.atomtype))







# class BenzylAlcohol(mb.Compound):
#     def __init__(self):
#         super(BenzylAlcohol, self).__init__()
#
#         mb.load('/Users/jonestj1/benzyl-alcohol.pdb', compound=self)
#
# benzyl_alcohol = BenzylAlcohol()
#
# traj = benzyl_alcohol.to_trajectory()
#
# benzyl_alcohol.save_gromacs(filename='benzyl-alcohol.gro', traj=traj)


# from mbuild.examples.pmpc.pmpc_brush_layer import PMPCLayer
# import mbuild as mb
#
# mask = mb.grid_mask_2d(5, 5)
#
# pmpc = PMPCLayer(mask)
#
# pmpc.save_gromacs(filename='pmpc_layer.gro', traj=pmpc.to_trajectory())

# from mbuild.examples.alkane.alkane import Alkane
#
# alkane = Alkane(n=5)
#
# alkane.save_gromacs(filename='alkane.gro', traj=alkane.to_trajectory())


# ## AlkaneMonolayer ###
# import mbuild as mb
# from mbuild.examples.alkane_monolayer.alkane_monolayer import AlkaneMonolayer
# import os
# import itertools
#
# chain_length = [6, 8, 10, 12, 14, 16]
# sqrt_number_chains = [4, 5, 6, 7, 8, 9, 10]
# for cl, sqrt_nc in itertools.product(chain_length, sqrt_number_chains):
#     mask = mb.grid_mask_2d(sqrt_nc, sqrt_nc)
#     alkane_monolayer = AlkaneMonolayer(chain_length=cl, mask=mask,)
#     traj = alkane_monolayer.to_trajectory()
#     # Account for 2d geometry
#     alkane_monolayer.periodicity[2] = alkane_monolayer.boundingbox.maxs[2] * 3
#     alkane_monolayer.save_gromacs(filename='{0}_{1}_alkane_monolayer.gro'.format(sqrt_nc**2, cl), traj=traj)
#
#     os.system("printf 'q\n' | gmx make_ndx -f {0}_{1}_alkane_monolayer -o index.ndx".format(sqrt_nc**2, cl))
#     with open('index.ndx', 'w') as index:
#         index.write('\n[ BottomSi ]\n'
#                     '   2   20   38   56   74   92  110  128  146  164  182  200  218  236  254 \n'
#                     ' 272  290  308  326  344  362  380  398  416  434  452  470  488  506  524 \n'
#                     ' 542  560  578  596  614  632  650  668  686  704  722  740  758  776  794 \n'
#                     ' 812  830  848  866  884  902  920  938  956  974  992 1010 1028 1046 1064 \n'
#                     '1082 1100 1118 1136 1154 1172 1190 1208 1226 1244 1262 1280 1298 1316 1334 \n'
#                     '1352 1370 1388 1406 1424 1442 1460 1478 1496 1514 1532 1550 1568 1586 1604 \n'
#                     '1622 1640 1658 1676 1694 1712 1730 1748 1766 1784\n')
#         index.close()
#     with open('run_file_{0}_{1}.sh'.format(sqrt_nc**2, cl), 'w') as run_file:
#         run_file.write('gmx grompp -f em-tiny.mdp -c {0}_{1}_alkane_monolayer.gro -p {0}_{1}_alkane_monolayer.top -n index.ndx -o em-tiny_{0}_{1}.tpr\n'
#                        'gmx mdrun -deffnm em-tiny_{0}_{1}\n'
#                        'gmx grompp -f em.mdp -c em-tiny_{0}_{1}.gro -p {0}_{1}_alkane_monolayer.top -n index.ndx -o em_{0}_{1}.tpr\n'
#                        'gmx mdrun -deffnm em_{0}_{1}\n'
#                        'gmx grompp -f nvt-tiny.mdp -c em_{0}_{1}.gro -p {0}_{1}_alkane_monolayer.top -n index.ndx -o nvt-tiny_{0}_{1}.tpr\n'
#                        'gmx mdrun -deffnm nvt-tiny_{0}_{1}\n'
#                        'gmx grompp -f nvt.mdp -c nvt-tiny_{0}_{1}.gro -p {0}_{1}_alkane_monolayer.top -n index.ndx -o nvt_{0}_{1}.tpr\n'
#                        'gmx mdrun -deffnm nvt_{0}_{1}\n'
#                        'gmx grompp -f production.mdp -c nvt_{0}_{1}.gro -p {0}_{1}_alkane_monolayer.top -n index.ndx -o production_{0}_{1}.tpr\n'
#                        'gmx mdrun -deffnm production_{0}_{1}\n'.format(sqrt_nc**2, cl))
#         run_file.close()
#     os.system('bash run_file_{0}_{1}.sh'.format(sqrt_nc**2, cl))
#     os.system('vmd nvt.gro production.trr')

### AlkaneMonolayers ###
import mbuild as mb
from mbuild.examples.alkane_monolayer.alkane_monolayer import AlkaneMonolayer
import itertools

chain_length = [6, 8, 10, 12, 14, 16, 18]
number_of_chains = [16, 25, 36, 49, 64, 81, 100]

for cl, nc in itertools.product(chain_length, number_of_chains):

    mask = mb.grid_mask_2d(nc**0.5, nc**0.5)
    alkane_monolayer = AlkaneMonolayer(chain_length=cl, mask=mask,)

    # Account for 2d geometry
    alkane_monolayer.periodicity[2] = alkane_monolayer.boundingbox.maxs[2] * 3

    traj = alkane_monolayer.to_trajectory()
    alkane_monolayer.save_gromacs(filename='{0}_{1}_alkane_monolayer.gro'
                                  .format(nc, cl), traj=traj)

### AlkaneMonolayers ###

chain_length = [6, 8, 10, 12, 14, 16, 18]
number_of_chains = [16, 25, 36, 49, 64, 81, 100]

for cl, nc in itertools.product(chain_length, number_of_chains):
    mask = mb.grid_mask_2d(nc**0.5, nc**0.5)
    alkane_monolayer = AlkaneMonolayer(chain_length=cl, mask=mask)

    alkane_monolayer.save(filename='{0}_{1}_alkane_monolayer.gro'
                          .format(nc, cl))