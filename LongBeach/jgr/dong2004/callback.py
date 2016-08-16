def add_gravel(model, L):
    t = model.get_current_time()
    
    if t == 0:
        n = int(10*L)
        mass = model.get_var('mass')
        mass[:,-n:,:,-1] = mass[:,-n:,:,:].sum(axis=3)
        mass[:,-n:,:,:-1] = 0.
        
        model.set_var('mass', mass)
        
                                                    
def add_gravel_0050(model):
    add_gravel(model, 0.5)

    
def add_gravel_0100(model):
    add_gravel(model, 1.)

    
def add_gravel_0200(model):
    add_gravel(model, 2.)

    
def add_gravel_0400(model):
    add_gravel(model, 4.)

    
def add_gravel_0600(model):
    add_gravel(model, 6.)

    
def add_gravel_0800(model):
    add_gravel(model, 8.)

    
def add_gravel_1000(model):
    add_gravel(model, 10.)

    
def add_gravel_1200(model):
    add_gravel(model, 12.)

    
