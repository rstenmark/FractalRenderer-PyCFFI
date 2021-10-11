# FractalRenderer-PyCFFI
A toy Mandelbrot set fractal renderer utilizing a multithreaded Escape Time algorithm and CFFI math routines.

# Requirements
Requires Python 3+, PIL, CFFI

You can acquire these modules via pip. Refer to CFFI documentation for installation instructions for your platform.

# Instructions
With all requirements installed, run fc_extension_build.py to compile the CFFI extension.

Run main.py. An image named "mandelbrot.png" will be written to the current working directory.
