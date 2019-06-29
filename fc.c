double * fc(double zr, double zi, double cr, double ci) {
    static double a[2];
    double zr_temp = (zr * zr - zi * zi);
    zi = (zr * zi + zi * zr);
    zr = zr_temp;
    zr = zr + cr;
    zi = zi + ci;
    a[0] = zr;
    a[1] = zi;
    return a;
}

int * mandelbrot(int x, int y, double zr, double zi, double cr, double ci, int r, int iterations) {
    cr = -2.5 + (cr / x) * (1 + abs(-2.5));
    ci = -1.5 + (ci / y) * (1.5 + abs(-1.5));

    for(int i=0; i<iterations; i++) {
        z = fc(zr, zi, cr, ci);
    }
}
