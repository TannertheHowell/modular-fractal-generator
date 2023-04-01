import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
from ImagePainter import paint
from time import time

# For convenience, I have placed these into a dictionary, so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'patternDict'.
patternDict = {
    'mandelbrot': {
        'centerX': -0.6,
        'centerY': 0.0,
        'axisLength': 2.5,
    },

    'mandelbrot-zoomed': {
        'centerX': -1.0,
        'centerY': 0.0,
        'axisLength': 1.0,
    },

    'spiral0': {
        'centerX': -0.761335372924805,
        'centerY': 0.0835704803466797,
        'axisLength': 0.004978179931102462,
    },

    'spiral1': {
        'centerX': -0.747,
        'centerY': 0.1075,
        'axisLength': 0.002,
    },

    'seahorse': {
        'centerX': -0.748,
        'centerY': -0.102,
        'axisLength': 0.008,
    },

    'elephants': {
        'centerX': 0.3015,
        'centerY': -0.0200,
        'axisLength': 0.03,
    },

    'leaf': {
        'centerX': -1.543577002,
        'centerY': -0.000058690069,
        'axisLength': 0.000051248888,
    },

    'starfish': {
        'centerX': -0.463595023481762,
        'centerY': 0.598380871135558,
        'axisLength': 0.00128413675654471,
    },
}


def mbrot_main(fractalName):
    """The main entry-point for the Mandelbrot fractal generator"""
    size = 512
    startTime = time()
    window = Tk()

    print("Rendering %s fractal" % fractalName, file=sys.stderr)

    tkPhotoImage = PhotoImage(width=size, height=size)
    # TODO: REFORMAT
    paint(patternDict, fractalName, window, tkPhotoImage, size)

    print(f"\nDone in {time() - startTime:.3f} seconds!", file=sys.stderr)
    tkPhotoImage.write(f"{fractalName}.png")
    print("Wrote picture " + fractalName + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()



