from Phoenix import Phoenix
from Julia import Julia
from Mandelbrot import Mandelbrot
from Mandelbrot3 import Mandelbrot3


def make_fractal(fractal_info):
    fractal_type = fractal_info.get('type')
    max_iterations = fractal_info.get('iterations')

    if fractal_type == 'mandelbrot':
        return Mandelbrot(max_iterations)
    elif fractal_type == 'phoenix':
        creal = fractal_info.get('creal')
        cimag = fractal_info.get('cimag')
        preal = fractal_info.get('preal')
        pimag = fractal_info.get('pimag')
        return Phoenix(max_iterations, creal, cimag, preal, pimag)
    elif fractal_type == 'mandelbrot3':
        return Mandelbrot3(max_iterations)
    elif fractal_type == 'julia':
        creal = fractal_info.get('creal')
        cimag = fractal_info.get('cimag')
        return Julia(max_iterations, creal, cimag)
