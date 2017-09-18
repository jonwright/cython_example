

import numpy, myinterface, time

N = 1024*1024*4*4
vecs = numpy.arange((N*3), dtype=float).reshape((N,3))
mods = numpy.ones(N, float)
print "Memory increment",(mods.nbytes+vecs.nbytes)/1024,"K"
start = time.time()
myinterface.py_vnorm( vecs, mods )
diff = time.time()-start
print diff,"/s",(mods.nbytes+vecs.nbytes)/1024/1024/diff,"MB/s"
print "Works? :",numpy.allclose( numpy.sqrt((vecs*vecs).sum(axis=1)), mods )


try:
    myinterface.py_vnorm( vecs[::2], mods[::2] )
except ValueError:
    print "Catches non-contiguous"

try:
    myinterface.py_vnorm( vecs.T, mods[::2] )
except ValueError:
    print "Catches transpose"

start = time.clock()
for i in range(1000):
    myinterface.py_vnorm( vecs[:1], mods[:1] )
print "Print, us per call for 1 value",(time.clock()-start)*1000

