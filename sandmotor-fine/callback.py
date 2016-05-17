import os
import logging
import numpy as np
from datetime import datetime, timedelta

current = None
t0 = datetime(2011,8,1)
    
# initialize logger
logger = logging.getLogger(__name__)


def update_bed(model):
    global current
    
    k = (t0 + timedelta(seconds=model.get_current_time())).strftime('%Y%m%d')
    if current is None or current != k:
        zb = model.get_var('zb')
        fname = 'bathy/z_%s.txt' % k
        if os.path.exists(fname):
            zb_new = zb.copy()
            zb_new[:,:] = np.loadtxt(fname)
            model.set_var('zb', zb_new)
            logger.info('Updated bathymetry to "%s"' % k)
            current = k
