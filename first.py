import numpy as np
def normalize_array(seed = 5):
    rg = np.random.default_rng(seed)

    # creating arrays with 4x4 dimension
    b = np.random.randint(0,20, size=16).reshape(4,4)

    diag_elemtns = np.diag(b)
    c = (diag_elemtns-np.min(diag_elemtns))/(np.max(diag_elemtns)-np.min(diag_elemtns))

    d = np.copy(b)
    np.fill_diagonal(d,c)
    
    return b,d

