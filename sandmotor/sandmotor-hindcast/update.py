import os
import numpy as np
import logging


# initialize time stamps
n = 0
tstamps = sorted([int(x[2:-4]) for x in os.listdir('bathy/') if x.startswith('z')])

# initialize logger
logger = logging.getLogger(__name__)


def update_bed(model):
    global n
    
    if n < len(tstamps):
        t = model.get_current_time()
        if t >= tstamps[n]:
            fname = 'bathy/z_%09d.txt' % tstamps[n]
            n = n + 1
            zb = model.get_var('zb')
            if os.path.exists(fname):
                zb_new = zb.copy()
                zb_file = np.loadtxt(fname)
                ix = zb_file < 0.
                zb_new[ix] = zb_file[ix]
                model.set_var('zb', zb_new)
                logger.info('Updated subtidal bathymetry from "%s"', fname)
                logger.debug('Updated %d of %d cells', np.sum(ix), len(ix.flatten()))
