

import cython

import numpy as np
cimport numpy as np

cdef extern from "my_c_code.h":
    void vnorm(double[], double[], int n)


def py_vnorm( np.ndarray[ double, ndim=2, mode='c'] vecs not None, 
           np.ndarray[ double, ndim=1] mods ):
    n = len( vecs )
    assert len( mods ) == n
    assert vecs.shape[1] == 3
    vnorm( &vecs[0,0], &mods[0], n)


