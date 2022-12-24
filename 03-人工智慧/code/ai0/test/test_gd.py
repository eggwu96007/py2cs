import numpy as np
import optimize as opt

def f(p):
    [x, y, z] = p
    return (x-1)**2+(y-2)**2+(z-3)**2

def test_gd():
    p = [0.0, 0.0, 0.0]
    opt.gd(f, p)
    assert np.allclose(p, [0.0]*len(p))
