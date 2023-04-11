def count_iterations(z, max_iter):
    """
    Return iteration count of the Phoenix set for a point 'z'
    """
    c = complex(0.5667, 0.0)
    phoenix = complex(-0.5, 0.0)
    zFlipped = complex(z.imag, z.real)
    zPrev = 0+0j
    z = zFlipped
    for i in range(max_iter):
        zSave = z
        z = z * z + c + (phoenix * zPrev)
        zPrev = zSave
        if abs(z) > 2.0:
            return i
    return max_iter - 1
