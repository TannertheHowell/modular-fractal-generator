def getColorFromPalette(z, grad):
    """
    Return the index of the color of the current pixel
    within the Phoenix fractal in the palette array
    z is the complex number passed in
    """

    # c is the Julia Constant; varying this value gives rise to a variety of variate images
    c = complex(0.5667, 0.0)

    # phoenix is the Phoenix Constant; same deal as above - adjust this to get different results
    phoenix = complex(-0.5, 0.0)

    # The first thing we do to the complex number Z is reflect its components,
    # so the imaginary part becomes the real part, and vice versa
    zFlipped = complex(z.imag, z.real)


    # zPrevious is the PREVIOUS Z value, except the 1st time through the
    # function, when it starts out as Complex Zero (which is actually the
    # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!
    zPrev = 0+0j
    # set Z back to zFlipped, it is literally super-important that we do this
    # before the next part of the algorithm
    z = zFlipped

    for i in range(102):
        zSave = z  # save the current Z value before we overwrite it
        # compute the new Z value from the current and previous Zs
        z = z * z + c + (phoenix * zPrev)
        zPrev = zSave  # Set the prevZ value for the next iteration

        # if the absolute value of Z is greater or equal than 2, then return that color
        if abs(z) > 2:
            return grad[i]  # The sequence is unbounded

    return grad[101]         # Else this is a bounded sequence
