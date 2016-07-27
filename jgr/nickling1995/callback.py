import numpy as np


def add_marbles(model, s):
    t = model.get_current_time()
    
    if t == 0:
        R = .009
        mass = model.get_var('mass')
        n = mass.shape[2]
        for i in range(1, n):
            z = i * .0002
            Ri = R * np.sin(np.arccos(np.maximum(-1.,(R-z)/R)))
            p = np.pi * Ri**2 / s**2
            if p > 1e-10:
                mass[:,:,i, -1] = mass[:,:,i,:].sum(axis=2) * p
                mass[:,:,i,:-1] = mass[:,:,i,:-1] * (1 - p)
            
        model.set_var('mass', mass)


def add_marbles_060(model):
    add_marbles(model, .060)

    
def add_marbles_030(model):
    add_marbles(model, .030)

    
def add_marbles_018(model):
    add_marbles(model, .018)

    
