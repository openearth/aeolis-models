import os
import numpy as np

dt = 3600*24+50*60 # update once per half tidal cycle
    
def update_bed(model):
    t = model.get_current_time()
    if np.mod(t-5*60*60, dt) < 60: # update topo when high tide
        zb = model.get_var('zb')
        fname = 'TopoBathy\model_series\z_epoch_%i.txt' % int(np.floor(t / dt))
        if os.path.exists(fname):
            zb_new = zb.copy()
            zb_new[:,:] = np.loadtxt(fname)
            model.set_var('zb', zb_new)
            print ' '
            print 'updating topo'
            print 'time = %i h %i min' % (int(t/60/60),(t-int(t/60/60)*60*60)/60)
            print 'z_epoch_%i.txt loaded' % int(np.floor(t / dt))
	    print ' '
#def update_TideInLake(model)
#    zs = model.get_var('zs')
#    ind=1
#    zs[ind] = -999
#    model.setvar['zs',zs]