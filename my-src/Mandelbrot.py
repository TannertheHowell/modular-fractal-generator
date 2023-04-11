def PixelColorOrIndex(c, palette):
    """
    Return the color of the current pixel within the Mandelbrot set
    - OR -
    Return the INDEX of the color of the pixel within the Mandelbrot set
    The INDEX corresponds to the iteration count of the for loop.
    """
    z = complex(0, 0)  # z0
    MAX_ITERATIONS = 115

    if palette is not None:
        length = len(palette)
        for i in range(length):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                if i >= len(palette):
                    i = len(palette) - 1
                return palette[i]

    # If a color scheme palette is NOT passed in, return the number of the color
    # Used for leaf pattern
    elif palette is None:
        length = MAX_ITERATIONS
        for i in range(length):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                if i == MAX_ITERATIONS:
                    i = MAX_ITERATIONS - 1
                return i
            elif abs(z) <= 2:
                continue

    if palette is None:
        return i
    elif i >= len(palette):
        i = len(palette) - 1
    return palette[i]  # The sequence is unbounded