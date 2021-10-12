# FractalRenderer-PyCFFI
A toy Mandelbrot set fractal renderer utilizing multiple cores via Python multiprocessing and a relatively performant escape-time algorithm written in C via CFFI.

# Requirements
Requires Python 3+, PIL, CFFI

# Instructions
With all requirements installed, run fc_extension_build.py to compile the CFFI extension.

Run main.py. An image named "mandelbrot.png" will be written to the current working directory.
