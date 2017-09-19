
#
#  Build with intel linux compiler
#
#  source /opt/intel/parallel_studio_xe_2018/psxevars.sh
#  LDSHARED="icc -fast -shared" CC="icc -fast" python setup.py build_ext --inplace --force
#  ... otherwise gcc is used


from setuptools import setup
from distutils.extension import Extension

from Cython.Build import cythonize
import numpy, sys
import numpy.distutils.core

RUN_CYTHON=False
if RUN_CYTHON:
    extn = ".pyx"
else:
    extn = ".c"

if sys.platform.find("win32")==0: # Wrong - should check compiler
    eca = ["-openmp",]
    ela = []
else:
    eca = ["-fopenmp",]
    ela = ["-fopenmp"]


sourcefiles = [ 'myinterface'+extn,
                'my_c_code.c' ]

extensions = [ 
        # Cython
        Extension("myinterface", sourcefiles,
           include_dirs=[ numpy.get_include(),],
           extra_compile_args=eca,
           extra_link_args=ela,
           ),
    ]

f2pyext = numpy.distutils.core.Extension("f2py_vnorm",
        sources = ["interface_f2py.pyf", "my_c_code.c"],
        include_dirs=[ numpy.get_include(),],
        extra_compile_args=eca,
        extra_link_args=ela)


numpy.distutils.core.setup(
    ext_modules = cythonize( extensions ) + [f2pyext,] ,
    cffi_modules = ["build_my_c_code.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
)
