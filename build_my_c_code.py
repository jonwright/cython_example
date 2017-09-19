
# in a separate file "package/foo_build.py"
import cffi, sys


if sys.platform.find("win32")==0: # Wrong - should check compiler
    eca = ["-openmp",]
    ela = []
else:
    eca = ["-fopenmp",]
    ela = ["-lgomp",]


ffibuilder = cffi.FFI()
ffibuilder.cdef(open("my_c_code.h").read())
ffibuilder.set_source(
        "ffi_interface", 
        open("my_c_code.h").read(),
        sources=["my_c_code.c",],
        extra_compile_args=eca,
        extra_link_args=ela,
        )

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
