__author__ = 'jonestj1'



import mbuild as mb
from mbuild.examples.alkane_monolayer.alkane_monolayer import AlkaneMonolayer
from mbuild.coordinate_transform import *
import math

# make two alkane monolayers
mask = mb.grid_mask_2d(10, 10)

alkane_monolayer_one = AlkaneMonolayer(chain_length=10, mask=mask)
alkane_monolayer_two = AlkaneMonolayer(chain_length=10, mask=mask)

alkane_monolayer_one.kind = 'Bottom AlkaneMonolayer'
alkane_monolayer_two.kind = 'Top AlkaneMonolayer'


# rotate and translate one monolayer over another
xyz = alkane_monolayer_two.boundingbox.maxs - alkane_monolayer_two.boundingbox.mins
xyz[2] = xyz[2] * 2.1
xyz[1] = 0

rotate_around_y(alkane_monolayer_two, math.pi)
translate(alkane_monolayer_two, xyz)


# add the adjacent monolayers to be in the same file
system = mb.Compound()
system.add(alkane_monolayer_one)
system.add(alkane_monolayer_two)

alkane_monolayer_one.save_gromacs('one monolayer', False)