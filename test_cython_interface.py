
from __future__ import print_function

import numpy, myinterface, time, sys

N = 1024*1024*4*4
vecs = numpy.arange((N*3), dtype=float).reshape((N,3))
mods = numpy.ones(N, float)
print ("Memory increment",(mods.nbytes+vecs.nbytes)/1024,"K")
start = time.time()
myinterface.py_vnorm( vecs, mods )
diff = time.time()-start
print (diff,"/s",(mods.nbytes+vecs.nbytes)/1024/1024/diff,"MB/s")
print ("Works? :",numpy.allclose( numpy.sqrt((vecs*vecs).sum(axis=1)), mods ))


try:
    myinterface.py_vnorm( vecs[::2], mods[::2] )
except ValueError:
    print( "Catches non-contiguous")

try:
    myinterface.py_vnorm( vecs.T, mods[::2] )
except ValueError:
    print( "Catches transpose")

start = time.clock()
for i in range(1000):
    myinterface.py_vnorm( vecs[:1], mods[:1] )
print ("Print, us per call for 1 value",(time.clock()-start)*1000)



try:
    import pyopencl
    from pyopencl.characterize import has_double_support
    ctx = pyopencl.create_some_context()
    if not has_double_support( ctx.devices[0] ):
        print("No opencl double precision support so quitting")
        sys.exit()
except:
    print ("You dont have pyopencl, so skipping that")
    raise

newmods = numpy.zeros( mods.shape, mods.dtype )
    
queue = pyopencl.CommandQueue( ctx )
mf = pyopencl.mem_flags

start = time.time()

if not hasattr( pyopencl, "SVM" ) :
    print("Using copies host to device" )
    v_g = pyopencl.Buffer( ctx, mf.READ_ONLY | mf.COPY_HOST_PTR ,
                       vecs.nbytes , 
                       hostbuf = vecs )
    m_g = pyopencl.Buffer( ctx, mf.WRITE_ONLY , newmods.nbytes )
    prg = pyopencl.Program( ctx,
                            open( "my_cl_code.cl", "r" ).read()
                        ).build()
    setuptime = time.time()-start
    start = time.time()
    prg.vnorm( queue, (N,), None, v_g, m_g )
    pyopencl.enqueue_read_buffer( queue, m_g, newmods).wait()
else:
    print("Avoiding copies")
    prg = pyopencl.Program( ctx,
                            open( "my_cl_code.cl", "r" ).read()
                        ).build()
    setuptime = time.time()-start
    start = time.time()
    prg.vnorm( queue, (N,), None, pyopencl.SVM( vecs ), pyopencl.SVM(newmods) )
    queue.finish()
               
runtime = time.time()- start

if (newmods - mods).max() == 0:
    print( "opencl seemed to work", setuptime, runtime)


