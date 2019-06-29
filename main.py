from PIL import Image
from collections import deque
import numpy as np
from multiprocessing import Pool, cpu_count
from _fc.lib import fc

def in_mandelbrot_set(xy, c, iterations):
    z = 0
    radius = 2
    max_periodicity = 10

    c_range = ((-2, 1), (-1.5, 1.5))

    # Transform c to (-2.5, 1) + (-1, 1)i
    c = complex(c_range[0][0] + (c.real / xy[0]) * (c_range[0][1] + abs(c_range[0][0])),
                c_range[1][0] + (c.imag / xy[1]) * (c_range[1][1] + abs(c_range[1][0])))
    #c *= 1.0

    for i in range(0, iterations):
        z = fc(z.real, z.imag, c.real, c.imag)
        z = complex(z[0], z[1])
        if abs(z) > radius:
            return (False, i)

    return (True, iterations)


def full_set_parallel(field, subdiv, max_iterations):
    # Parallel implementation
    args = []
    for j in range(0, subdiv):
        for i in range(0, subdiv):
            args.append( ((subdiv, subdiv), complex(j, i), max_iterations) )
    print("done building arguments")

    p = Pool(cpu_count())
    r = list(p.starmap(in_mandelbrot_set, args))

    for j in range(0, subdiv):
        for i in range(0, subdiv):
            ind = (subdiv*j) + i
            if r[ind][0]:
                field[j][i] = 0 * r[ind][1]/max_iterations
            else:
                field[j][i] = 255 * r[ind][1]/max_iterations

def lbl_parallel(field, subdiv, max_iterations):
    # Line-by-line Parallel implementation
    args = []
    p = Pool(cpu_count())
    for j in range(0, subdiv):
        for i in range(0, subdiv):
            args.append( ((subdiv, subdiv), complex(j, i), max_iterations) )

        r = list(p.starmap(in_mandelbrot_set, args))

        for i in range(0, subdiv):
            if r[i][0]:
                field[j][i] = 0
            else:
                field[j][i] = 255 * r[i][1]/max_iterations

        args = []

def serial(field, subdiv, max_iterations):
    # Serial implementation
    with np.nditer(field, flags=['multi_index']) as it:
        
        while not it.finished:
            i, j = it.multi_index[0], it.multi_index[1]
            c = complex(j, i)
            r = in_mandelbrot_set((subdiv, subdiv), c, iterations=max_iterations) 
            if r[0]:
                field[j][i] = 0 * r[1]/max_iterations
            else:
                field[j][i] = 255 * r[1]/max_iterations
            it.iternext()

if __name__ == '__main__':
    max_iterations = 64
    subdiv = 2048
    field = np.zeros((subdiv, subdiv), dtype=int)

    print(subdiv, "x", subdiv, ", maximum iterations: ", max_iterations, sep='')
    lbl_parallel(field, subdiv, max_iterations)


    im = Image.new('RGB', (subdiv, subdiv))
    for j in range(0, len(field)):
        for i in range(0, len(field[0])):
            r = int(field[j][i])
            g = int(field[j][i]/2)
            b = int(field[j][i]/4)
            im.putpixel((j, i), (r, g, b))

    im.save("mandelbrot.png")
