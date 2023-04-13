from Phoenix import Phoenix
from Julia import Julia
from Mandelbrot import Mandelbrot
from OrientalDragons import OrientalDragons


def make_fractal(fractal):
    fractal_type = fractal.get('type')
    max_iterations = fractal.get('iterations')

    if fractal_type == 'OrientalDragons':
        # TODO this feels redundant with the c,
        # how can I set it ip like mbrot and phoenix to just use c inside of count?
        c = fractal.get('c', -0.8 + 0.156j)
        return OrientalDragons(max_iterations, c)
    elif fractal_type == 'Mandelbrot':
        return Mandelbrot(max_iterations)
    elif fractal_type == 'Phoenix':
        return Phoenix(max_iterations)
    elif fractal_type == 'Julia':
        c = fractal.get('c', -0.8 + 0.156j)
        return Julia(max_iterations, c)
    else:
        # TODO do a default fractal hard coded in
        return
