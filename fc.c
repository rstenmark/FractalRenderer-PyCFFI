#include <stdlib.h>
#include <math.h>
int * mandelbrot(int x1, int y1, int x2, int y2, int x_slice, int x_max, int y_max, int iterations, double radius) {
    //int * ret[y2 - y1][x2 - x1];
    // Image is sliced vertially so y1 and y2 are equal and constant
    int* ret = (int*)malloc(x_slice * y2 * sizeof(int));
    
    //static int ret[279936]; 
    double zr;
    double zi;
    double cr;
    double ci;
    double zr_temp;

    for(int y = y1; y < y2; y++) {
        for(int x = x1; x < x2; x++) {
            // Transform XY coordinates to complex coordinates
            zr = 0.0;
            zi = 0.0;
            cr = -2.0 + ( (float)y / (float)(y_max) ) * 3.0;
            ci = -1.5 + ( (float)x / (float)(x_max) ) * 3.0;

            for(int i=0; i<iterations; i++) {
                zr_temp = (zr * zr - zi * zi);
                zi = (zr * zi + zi * zr);
                zr = zr_temp;
                zr = zr + cr;
                zi = zi + ci;
                ret[y * x_slice + x - x1] = i;

                if(sqrt(zr * zr + zi * zi) > radius) {
                    break;
                }
            }
        }
    }
    return ret;
}