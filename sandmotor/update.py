import os
import numpy as np

dt = 3600*24*1 # update once a week
    
def update_bed(model):
    t = model.get_current_time()
    if np.mod(t, dt) < 3600:
        zb = model.get_var('zb')
        fname = 'bathy/z_%d.txt' % int(np.floor(t / dt))
        if os.path.exists(fname):
            zb_new = zb.copy()
            zb_new[:,:] = np.loadtxt(fname)
            model.set_var('zb', zb_new)

def update_TideInLake(model)
    zs = model.get_var('zs')
    ind=1
    zs[ind] = -999
    model.setvar['zs',zs]