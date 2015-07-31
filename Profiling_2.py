__author__ = 'jonestj1'
from memory_profiler import profile

@profile()
def fun():
    import mbuild as mb
    import numpy as np
    from mbuild.examples.pmpc.pmpc_brush_layer import PMPCLayer

    PMPCLayer(mask=mb.grid_mask_2d(10, 10), chain_length=10, alpha=np.pi/4,
          tile_x=3, tile_y=3)

if __name__=="__main__":
    fun()