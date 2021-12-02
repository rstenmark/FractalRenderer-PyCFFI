# Mandelbrot-Python-MP-CFFI
An exercise in using Python's multiprocessing module and C FFI to calculate a [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set) as fast as possible.

Currently the script is "fast enough", and can calculate fairly large sets (50k * 50k) quickly, but is bottlenecked by the host's RAM capacity. Writing the set to disk as an image will commonly take longer than calculating the set due to the calculation results being passed back from C into Python and then written one pixel at a time into a Pillow Image object and then saved. Obviously, improvements could be made here :)

# Requirements
Requires Python 3+, Pillow, CFFI

# Instructions
With all requirements installed, run fc_extension_build.py to compile the CFFI extension.

Run main.py. An image named "mandelbrot.png" will be written to the current working directory.
