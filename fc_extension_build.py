#!/usr/bin/python3

from cffi import FFI
ffibuilder = FFI()
ffibuilder.cdef("""int * mandelbrot(int x1, int y1, int x2, int y2, int x_slice, int x_max, int y_max, int iterations, double radius);""")

ffibuilder.set_source("_fc",
    """ 
    #include "fc.h"
    """,
    sources=["fc.c"])

ffibuilder.compile(verbose=True)