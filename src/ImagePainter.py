import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time

from Palette import palette, grad
import Mandelbrot
import Phoenix


def imagePainterMain(fractalName, fractalInfo):
    """The main entry-point for the fractal generator"""
    size = 512
    startTime = time()
    window = Tk()

    print("Rendering %s fractal" % fractalName, file=sys.stderr)

    tkPhotoImage = PhotoImage(width=size, height=size)
    paint(fractalName, fractalInfo, window, tkPhotoImage, size, grad)

    print(f"\nDone in {time() - startTime:.3f} seconds!", file=sys.stderr)
    tkPhotoImage.write(f"{fractalName}.png")
    print("Wrote picture " + fractalName + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()


def paint(fractalName, fractalInfo, window, tkPhotoImage, size, grad):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	  	  
    This code creates an image which is 640x640 pixels in size."""

    minx = fractalInfo['centerX'] - (fractalInfo['axisLength'] / 2.0)
    maxx = fractalInfo['centerX'] + (fractalInfo['axisLength'] / 2.0)
    miny = fractalInfo['centerY'] - (fractalInfo['axisLength'] / 2.0)
    maxy = fractalInfo['centerY'] + (fractalInfo['axisLength'] / 2.0)

    # Display the image on the screen
    tk_canvas = Canvas(window, width=size, height=size, bg='#000000')
    tk_canvas.pack()
    tk_canvas.create_image((size / 2, size / 2), image=tkPhotoImage, state="normal")

    pixelSize = abs(maxx - minx) / size

    for row in range(size, 0, -1):
        paletteList = []
        for col in range(size):
            x = minx + col * pixelSize
            y = miny + row * pixelSize
            # "Leaf" is the only well-behaved fractal - all of the others crash
            #
            if fractalName in ['leaf', ]:
                idx = PixelColorOrIndex(complex(x, y), None)
                color = palette[idx]
            # The rest of the fractals
            else:
                if fractalInfo["type"] == "phoenix":
                    color = getColorFromPalette(complex(x, y), grad)
                else:
                    color = PixelColorOrIndex(complex(x, y), palette)

            paletteList.append(color)

        pixels = '{' + ' '.join(paletteList) + '}'
        tkPhotoImage.put(pixels, (0, size - row))
        window.update()  # display a row of pixels

        print(pixelsWrittenSoFar(row, size), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column


def pixelsWrittenSoFar(rows, size):
    portion = (size - rows) / size
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))


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


# def makePictureOfFractal(fractal, window, grad, tkPhotoImage, backgroundColor, size):
#     """Paint a Fractal image into the TKinter PhotoImage canvas.
#     Assumes the image is 640x640 pixels."""
#
#     minx = fractal['centerX'] - (fractal['axisLength'] / 2.0)
#     maxx = fractal['centerX'] + (fractal['axisLength'] / 2.0)
#     miny = fractal['centerY'] - (fractal['axisLength'] / 2.0)
#     maxy = fractal['centerY'] + (fractal['axisLength'] / 2.0)
#
#     # Display the image on the screen
#     tk_canvas = Canvas(window, width=size, height=size, bg=backgroundColor)
#     tk_canvas.pack()
#
#     tk_canvas.create_image((size / 2, size / 2), image=tkPhotoImage, state="normal")
#
#     pixelSize = abs(maxx - minx) / size
#
#     for row in range(size, 0, -1):
#         paletteList = []
#         for col in range(size):
#             x = minx + col * pixelSize
#             y = miny + row * pixelSize
#
#             color = getColorFromPalette(complex(x, y), grad)
#             paletteList.append(color)
#
#         pixels = '{' + ' '.join(paletteList) + '}'
#         tkPhotoImage.put(pixels, (0, size - row))
#         window.update()
#         print(pixelsWrittenSoFar(row, size), end='\r', file=sys.stderr)

