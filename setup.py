


from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy 



sourcefiles = [ 'myinterface.pyx',
                'my_c_code.c' ]

extensions = [ Extension("myinterface", sourcefiles,
       include_dirs=[ numpy.get_include(),],
       extra_compile_args=['-openmp']
       )
    ]

setup(
    ext_modules = cythonize( extensions )
)
