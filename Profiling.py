__author__ = 'jonestj1'
import cProfile, pstats, io
pr = cProfile.Profile()
pr.enable()
from mbuild.examples.pmpc.pmpc_brush_layer import PMPCLayer
import mbuild as mb
import numpy as np
PMPCLayer(mask=mb.grid_mask_2d(10, 10), chain_length=10, alpha=np.pi/4,
          tile_x=3, tile_y=3)
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

