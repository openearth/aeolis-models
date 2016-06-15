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
        if update_var(model, 'zb', 'bathy/z_%s.txt' % k):
            logger.info('Updated bathymetry to "%s"' % k)
            current = k
        if update_var(model, 'mask', 'bathy/mask_%s.txt' % k, dtype=np.complex):
            logger.info('Updated mask to "%s"' % k)
            

def update_var(model, var, fname, dtype=np.float):
    if os.path.exists(fname):
        try:
            val = model.get_var(var, clear=False)
            val_new = val.copy()
            val_new[:,:] = np.loadtxt(fname, dtype=dtype)
            model.set_var(var, val_new)
            return True
        except:
            return False
    else:
        return False
