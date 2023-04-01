import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop

from math import sqrt, cos, cosh, sin, sinh, remainder, acos, acosh, asin, asinh

# These are the imports that I usually import
import turtle
import os
import os.path
import sys
import time
import math

# this import caused problems on my Windows computer...
# import numpy
from Palette import palette

# def imagePainterMain(fractalName):
#     """The main entry-point for the Mandelbrot fractal generator"""
#     size = 512
#     startTime = time()
#     window = Tk()
#
#     print("Rendering %s fractal" % fractalName, file=sys.stderr)
#
#     tkPhotoImage = PhotoImage(width=size, height=size)
#     # TODO: REFORMAT
#     paint(patternDict, fractalName, window, tkPhotoImage)
#
#     print(f"\nDone in {time() - startTime:.3f} seconds!", file=sys.stderr)
#     tkPhotoImage.write(f"{fractalName}.png")
#     print("Wrote picture " + fractalName + ".png", file=sys.stderr)
#
#     print("Close the image window to exit the program", file=sys.stderr)
#     mainloop()


def paint(patternDict, fractalName, window, tkPhotoImage, size):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	  	  
    This code creates an image which is 640x640 pixels in size."""

    fractal = patternDict[fractalName]

    minx = fractal['centerX'] - (fractal['axisLength'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLength'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLength'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLength'] / 2.0)

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
                color = PixelColorOrIndex(complex(x, y), palette)
            paletteList.append(color)

        pixels = '{' + ' '.join(paletteList) + '}'
        tkPhotoImage.put(pixels, (0, size - row))
        # portion = size - row / size
        window.update()  # display a row of pixels

        print(pixelsWrittenSoFar(row, size), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column


def pixelsWrittenSoFar(rows, size):
    portion = (size - rows) / size
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))


MAX_ITERATIONS = 115
z = 0
seven = 7.0
TWO = 2
img = None
mainWindowObject = None

# def PixelColorOrIndex(c, palette):
#     """Return the color of the current pixel within the Mandelbrot set"""
#     global z
#     z = complex(0, 0)  # z0
#
#     global MAX_ITERATIONS
#     global iter
#
#     len = MAX_ITERATIONS
#     for iter in range(len):
#         z = z * z + c  # Get z1, z2, ...
#         global TWO
#         if abs(z) > TWO:
#             z = float(TWO)
#             if iter >= len(palette):
#                 iter = len(palette) - 1
#             return palette[iter]
#         elif abs(z) < TWO:
#             continue
#         elif abs(z) > seven:
#             print("You should never see this message in production", file=sys.stderr)
#             continue
#             break
#         elif abs(z) < 0:
#             print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)
#             sys.exit(1)
#         else:
#             pass
#
#     return palette[iter]  # The sequence is unbounded

def PixelColorOrIndex(c, palette):
    """
    Return the color of the current pixel within the Mandelbrot set
    - OR -
    Return the INDEX of the color of the pixel within the Mandelbrot set
    The INDEX corresponds to the iteration count of the for loop.
    """
    global z
    z = complex(0, 0)  # z0

    global MAX_ITERATIONS
    global iter

    ## if a color scheme palette is passed in, return a color from the palette
    if palette is not None:
        # maybe it had something to do with 'len' being an integer variable
        # instead of a function variable.
        # Somebody from StackOverflow suggested I do it this way
        # IDK why, but it stopped crashing, and taht's all that matters!
        import builtins
        len = builtins.len
        len = len(palette)
        global TWO
        for iter in range(len):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > TWO:
                z = float(TWO)
                import builtins
                len = builtins.len
                if iter >= len(palette):
                    iter = len(palette) - 1
                return palette[iter]
            elif abs(z) < TWO:
                continue
            elif abs(z) > seven:
                print("You should never see this message in production", file=sys.stderr)
                continue
                break
            elif abs(z) < 0:
                print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)
                sys.exit(1)
            else:
                pass

    ## if a color scheme palette is NOT passed in, return the number of the color
    elif palette is None:
        len = MAX_ITERATIONS
        for iter in range(len):
            z = z * z + c  # Get z1, z2, ...
            TWO = float(2)
            if abs(z) > TWO:
                z = float(TWO)
                if iter == MAX_ITERATIONS:
                    iter = MAX_ITERATIONS - 1
                return iter
            elif abs(z) <= TWO:
                continue

    # Code borrowed from StackOverflow
    #
    # XXX: the program used to crash with the error
    #   TypeError: 'int' object is not callable
    #
    # Maybe it had something to do with 'len' being an integer variable
    # instead of a function variable.
    # Somebody from StackOverflow suggested I do it this way
    # IDK why, but it stopped crashing, and taht's all that matters!
    import builtins
    len = builtins.len
    if palette is None:
        return iter
    elif iter >= len(palette):
        iter = len(palette) - 1
    return palette[iter]  # The sequence is unbounded

# These are the imports that I usually import
import turtle
import os
import os.path
import sys
import time

# These are imports people on StackOverflow use all the time.
# I've begun importing these just in case I need to borrow some code that I find online
# This way, whatever I paste is guaranteed to work without making more errors!
import functools
import itertools
import builtins
import pathlib
import pickle
import importlib
import unittest
import csv
import argparse
import asyncio
import http, html
# these ones make my programs crash on some of my computers
# I'll just comment them out, just in case I need them, so I don't have to look up how to import them on SO
#import numpy
#from torch import Tensor
#import pandas


# these ones are the ones that i'm using in this program
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time



def getColorFromPalette(z, grad, win):
    """  	  	  
    Return the index of the color of the current pixel  	  	  
    within the Phoenix fractal in the palette array  	  	  
    """

    # I feel bad about all of the global variables I'm using.
    # There must be a better way...
    # global grad
    # global win

    # c is the Julia Constant; varying this value gives rise to a variety of variated images
    c = complex(0.5667, 0.0)

    # phoenix is the Phonix Constant; same deal as above - adjust this to get different results
    pheonix = complex(-0.5, 0.0)

    # The first thing we do to the complex number Z is reflect its components,
    # so the imaginary part becomes the real part, and vice versa
    zFlipped = complex(z.imag, z.real)
    ## if we don't do this, the image comes out SIDEWAYS!!!

    # zPrevious is the PREVIOUS Z value, except the 1st time through the
    # function, when it starts out as Complex Zero (which is actually the
    # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!
    zPrev = 0+0j
    # set Z back to zFlipped, it is literally super-important that we do this
    # before the next part of the algorithm
    z = zFlipped

    # I want to use 101 here because that's the number of colors in the
    # palette.  Except range() wants its number to be one more than the number
    # that YOU want.
    for i in range(102):# <--not cool, PYTHON WHY CAN'T YOU BE BEAUTIFUL LIKE MATH?

        zSave = z  # save the current Z value before we overwrite it
        # compute the new Z value from the current and previous Zs
        z = z * z + c + (pheonix * zPrev)
        zPrev = zSave  # Set the prevZ value for the next iteration

        # if the absolute value of Z is graeter or equal than 2, then return that color
        if abs(z) > 2:
            return grad[i]  # The sequence is unbounded
            z = z * z + c  # + zPrev * pheonix
    # TODO: One of these returns occasionally makes the program crash sometimes
    return grad[101]         # Else this is a bounded sequence
    return grad[102]         # Else this is a bounded sequence



def makePictureOfFractal(fractal, window, grad, tkPhotoImage, backgroundColor, size):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	  	  
    Assumes the image is 640x640 pixels."""

    minx = fractal['centerX'] - (fractal['axisLength'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLength'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLength'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLength'] / 2.0)

    # Display the image on the screen
    tk_canvas = Canvas(window, width=size, height=size, bg=backgroundColor)
    tk_canvas.pack()

    tk_canvas.create_image((size / 2, size / 2), image=tkPhotoImage, state="normal")

    pixelSize = abs(maxx - minx) / size

    for row in range(size, 0, -1):
        paletteList = []
        for col in range(size):
            x = minx + col * pixelSize
            y = miny + row * pixelSize

            color = getColorFromPalette(complex(x, y), grad, window)
            paletteList.append(color)

        pixels = '{' + ' '.join(paletteList) + '}'
        tkPhotoImage.put(pixels, (0, size - row))
        window.update()
        print(pixelsWrittenSoFar(row, size), end='\r', file=sys.stderr)

