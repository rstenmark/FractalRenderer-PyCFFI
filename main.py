#!/usr/bin/python3

import multiprocessing as mp
import math
from PIL import Image
from _fc.lib import mandelbrot

def f(args: tuple):
    print(*args)
    a = mandelbrot(*args)
    return [a[i] for i in range(0, (args[4] * args[3]))]

def main() -> None:
    # number of host CPUs
    cpus = mp.cpu_count()

    # image resolution
    resolution = (6**5, 6**5)

    # escape-time iterations per pixel
    iterations = 256

    # use unsigned 16-bit pixels
    image_mode = 'I;16'

    # brightness factor
    # multiply result pixel values by this value to maximize dynamic range
    # with PIL.Image in 'I;16' mode (16 bits per pixel, BW)
    brightness_factor = round(2**16 / iterations)

    # escape radius
    radius = 2.0

    # rectangular chunk size allocated to each core
    chunksize = (int(resolution[0]/cpus), resolution[1])

    # Build list of 9-tuples containing arguments to pass to mandelbrot func
    jobs = list()
    for i in range(0, cpus):
        jobs.append(
            (i * chunksize[0], 
            0, 
            (i+1)*chunksize[0], 
            chunksize[1],
            chunksize[0],
            resolution[0],
            resolution[1],
            iterations,
            radius)
        )

    # Map func over jobs
    with mp.Pool(cpus) as p:
        r = p.map(f, jobs)

    im = Image.new(image_mode, resolution)
    # For each result list
    for l, offset in zip(r, range(0, cpus)):
        # For each pixel in result list
        for i in range(0, chunksize[0] * chunksize[1]):
            xy = ((i % chunksize[0]) + chunksize[0]*offset, math.floor(i / chunksize[0]))
            im.putpixel(xy, brightness_factor * l[i])

    im.save("mandelbrot.png")

if __name__ == '__main__':
    main()