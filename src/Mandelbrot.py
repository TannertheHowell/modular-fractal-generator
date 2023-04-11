def count_iterations(c, max_iter):
    """
    Return iteration count of the Mandelbrot set for a point 'c'
    """
    z = complex(0, 0)  # z0
    for i in range(max_iter):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2.0:
            return i
    return max_iter - 1
