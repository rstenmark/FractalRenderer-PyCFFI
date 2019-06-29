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
