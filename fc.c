int * is_in_mbset(double zr, double zi, double cr, double ci, int iterations, double radius) {
    static int result[2];
    for(int i=0; i<iterations; i++) {

        double zr_temp = (zr * zr - zi * zi);
        zi = (zr * zi + zi * zr);
        zr = zr_temp;
        zr = zr + cr;
        zi = zi + ci;

        if(sqrt(zr * zr + zi * zi) > radius) {
            result[0] = 0;
            result[1] = i;
            return result;
        }
    }
    result[0] = 1;
    result[1] = iterations;
    return result;
}
