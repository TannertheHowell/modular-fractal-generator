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

def paint(fractals, imagename, window, img):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	  	  
    This code creates an image which is 640x640 pixels in size."""

    # global palette
    # global img

    fractal = fractals[imagename]

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=512, height=512, bg='#000000')
    canvas.pack()
    canvas.create_image((256, 256), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 512

    portion = 0
    total_pixels = 512 * 512  # 262144
    # loop
    for row in range(512, 0, -1):
        cc = []
        for col in range(512):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            # "Leaf" is the only well-behaved fractal - all of the others crash
            #
            if imagename in [ 'leaf', ]:
                idx = PixelColorOrIndex(complex(x, y), None)
                color = palette[idx]
            # The rest of the fractals
            else:
                color = PixelColorOrIndex(complex(x, y), palette)
            cc.append(color)
            y = miny + row * pixelsize # prepare for next loop
            x = minx + col * pixelsize # prepare for next loop

        img.put('{' + ' '.join(cc) + '}', to=(0, 512-row))
        portion = 512 - row / 512
        window.update()  # display a row of pixels

        portion = 512 - row / 512 # prepare for next loop
        # pixelsWrittenSoFar(portion, )  # This way isn't working let me try somthing eles...
        #total_pixles = pixelsWrittenSoFar(row, col)  # will equal 262144 when the program is finished
        print(pixelsWrittenSoFar(row, col), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column


def pixelsWrittenSoFar(rows, cols):
    portion = (512 - rows) / 512
    pixels = (512 - rows) * 512
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    # print(f"{pixels} pixels have been output so far")
    # return pixels
    # return '[' + status_percent + ' ' + status_bar + ']'
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))


# def pixelsWrittenSoFar(rows, cols):
#     pixels = 0
#     for r in range(rows + 1):
#         pixels = pixels + cols
#     print(pixels, "pixels have been output so far", file=sys.stderr)
#     return pixels

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




def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	  	  
    Assumes the image is 640x640 pixels."""
    win = w
    grad = g
    # Correlate the boundaries of the PhotoImage object to the complex
    # coordinates of the imaginary plane

    # Compute the minimum coordinate of the picture
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),
           (f['centerY'] - (f['axisLength'] / 2.0)))

    #global s  # huh, this worked last week...

    # Compute the maximum coordinate of the picture
    # The program has only one axisLength because the images are square
    # Squares are basically rectangles except the sides are equal instead of different
    max = ((f['centerX'] + (f['axisLength'] / 2.0)),
           (f['centerY'] + (f['axisLength'] / 2.0)))

    # Display the image on the screen
    tk_Interface_PhotoImage_canvas_pixel_object = Canvas(win, width=s, height=s, bg=W)

    # pack the canvas object into its parent widget
    tk_Interface_PhotoImage_canvas_pixel_object.pack()
    # TODO: Sometimes I wonder whether some of my functions are trying to do
    #       too many different things... this is the correct part of the
    #       program to create a GUI window, right?

    # Create the TK PhotoImage object that backs the Canvas Objcet
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.

    # Total number of pixels in the image, AKA the area of the image, in pixels
    area_in_pixels = 640 * 640

    # pack the canvas object into its parent widget
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Does this even matter?
    # At this scale, how much length and height of the
    # imaginary plane does one pixel cover?
    size = abs(max[0] - min[0]) / s

    # pack the canvas object into its parent widget
    tk_Interface_PhotoImage_canvas_pixel_object.pack()

    # Keep track of the fraction of pixels that have been written up to this point in the program
    fraction_of_pixels_writtenSoFar = int(s // 640)

    # for r (where r means "row") in the range of the size of the square image,
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to
    # but I have to here because we're actually going BACKWARDS, which took me
    # a long time to figure out, so don't change it, or else the picture won't
    # come out right
    r = s
    while r in range(s, 0, -1):
        # for c (c == column) in the range of pixels in a square of size s
        cs = []
        for c in range(s):
            # calculate the X value in the complex plane (I guess that's
            # actually the REAL number part, but we call it X because
            # GRAPHICS... whatev)
            X = min[0] + c * size
            Y = 0
            # get the color of the pixel at this point in the complex plain
            cp = getColorFromPalette(complex(X, Y), grad, win)
            # calculate the X value in the complex plane (but I know this is
            # really the IMAGINARY axis that we're talking about here...)
            Y = min[1] + r * size
            # TODO: do I really need to call getColorFromPalette() twice?
            #       It seems like this should be slow...
            #       But, if it aint broken, don't repair it, right?
            cp = getColorFromPalette(complex(X, Y), grad, win)
            cs.append(cp)
        pixls = '{' + ' '.join(cs) + '}'
        p.put(pixls, (0, s - r))
        w.update()  # display a row of pixels
        fraction_of_pixels_writtenSoFar = (s - r) / s # update the number of pixels output so far
        # print a statusbar on the console
        print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"
                + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",
                end="\r"  # the end
                , file=sys.stderr)
        r -= 1
