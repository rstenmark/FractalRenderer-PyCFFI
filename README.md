# FractalRenderer-PyCFFI
A toy Mandelbrot set fractal renderer utilizing multiple threads and CFFI math routines.

# Requirements
Requires Python 3+, PIL, numpy, CFFI

You can acquire these modules via pip. Refer to CFFI documentation for installation instructions for your platform.

# Instructions
With all requirements installed, run fc_extension_build.py to compile the CFFI extension.

Configure image parameters in main.py via the max_iterations and subdiv variables.

Run main.py. An image named "mandelbrot.png" will be written to the current working directory.

# Example

![mandelbrot](https://i.imgur.com/28sX6GQ.png)

2048x2048 with up to 64 iterations per pixel, rendered in 53.4 seconds on 4 threads on a AMD Phenom II x4 960T @ 3.8 GHz.
