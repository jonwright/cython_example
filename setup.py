
#
#  Build with intel linux compiler
#
#  source /opt/intel/parallel_studio_xe_2018/psxevars.sh
#  LDSHARED="icc -fast -shared" CC="icc -fast" python setup.py build_ext --inplace --force
#  ... otherwise gcc is used


from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy, sys

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

extensions = [ Extension("myinterface", sourcefiles,
       include_dirs=[ numpy.get_include(),],
       extra_compile_args=eca,
       extra_link_args=ela,
       )
    ]

setup(
    ext_modules = cythonize( extensions )
)
