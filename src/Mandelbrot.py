import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
from ImagePainter import paint
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

# These are the different views of the Mandelbrot set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.
images = {
    'mandelbrot': {
        'centerX': -0.6,
        'centerY': 0.0,
        'axisLen': 2.5,
    },

    'mandelbrot-zoomed': {
        'centerX': -1.0,
        'centerY': 0.0,
        'axisLen': 1.0,
    },

    'spiral0': {
        'centerX': -0.761335372924805,
        'centerY': 0.0835704803466797,
        'axisLen': 0.004978179931102462,
    },

    'spiral1': {
        'centerX': -0.747,
        'centerY': 0.1075,
        'axisLen': 0.002,
    },

    'seahorse': {
        'centerX': -0.748,
        'centerY': -0.102,
        'axisLen': 0.008,
    },

    'spiral1': {
        'centerX': -0.747,
        'centerY': 0.1075,
        'axisLen': 0.002,
    },

    'elephants': {
        'centerX': 0.3015,
        'centerY': -0.0200,
        'axisLen': 0.03,
    },

    'leaf': {
        'centerX': -1.543577002,
        'centerY': -0.000058690069,
        'axisLen': 0.000051248888,
    },

    'starfish': {
        'centerX': -0.463595023481762,
        'centerY': 0.598380871135558,
        'axisLen': 0.00128413675654471,
    },
}


def mbrot_main(image):
    global img
    # Set up the GUI so that we can paint the fractal image on the screen
    print("Rendering {} fractal".format(image), file=sys.stderr)
    before = time.time()
    global window
    window = Tk()
    img = PhotoImage(width=512, height=512)
    paint(images, image, window)

    # Save the image as a PNG
    after = time.time()
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{image}.png")
    print(f"Wrote picture {image}.png", file=sys.stderr)

    # Call tkinter.mainloop so the GUI remains open
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()



