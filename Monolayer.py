__author__ = 'Trev'

import mbuild as mb

from mbuild.examples.alkane.alkane import Alkane
from mbuild.components.small_groups.silane import Silane


class AlkylSilane(mb.Compound):
    """A silane functionalized alkane chain with one Port. """
    def __init__(self, chain_length):
        super(AlkylSilane, self).__init__()

        alkane = Alkane(chain_length, cap_end=False)
        self.add(alkane, 'alkane')
        silane = Silane()
        self.add(silane, 'silane')
        mb.equivalence_transform(self.alkane, self.alkane.down, self.silane.up)

        # Hoist silane port to AlkylSilane level.
        self.add(silane.down, 'down', containment=False)


from mbuild.tools.tiled_compound import TiledCompound
from mbuild.components.surfaces.betacristobalite import Betacristobalite

surface = Betacristobalite()
tiled_surface = TiledCompound(surface, n_tiles=(2, 3, 1), kind="tiled_surface")

from mbuild.components.atoms.H import H
alkylsilane = AlkylSilane(chain_length=10)
hydrogen = H()

from mbuild.tools.mask import grid_mask_2d
mask = grid_mask_2d(8, 8)  # Evenly spaced, 2D grid of points.

# Attach chains to specified binding sites. Other sites get a hydrogen.
mb.apply_mask(host=tiled_surface, guest=alkylsilane, mask=mask, backfill=hydrogen)

tiled_surface.visualize()