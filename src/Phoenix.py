import sys
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop
from ImagePainter import makePictureOfFractal
from Palette import grad, GREY0

from ImagePainter import paint
from math import sqrt, cos, cosh, sin, sinh, remainder, acos, acosh, asin, asinh

# These are the imports that I usually import
import turtle
import os
import os.path
import sys
from time import time
import math

# this import caused problems on my Windows computer...
# import numpy

s = 512
Save_As_Picture = True
tkPhotoImage = None

def phoenix_main(i):
    """The main entry-point for the Phoenix fractal generator"""

    # the size of the image we will create is 512x512 pixels
    # Look, I  know globals are bad, but I don't know how else to use those
    # variables in here if I don't do it this way.  I didn't take any fancy CS
    # classes, sue me
    global tkPhotoImage
    global win
    global s

    # Note the time of when we started so we can measure performance improvements
    b4 = time()
    # Set up the GUI so that we can display the fractal image on the screen
    win = Tk()

    print("Rendering %s fractal" % i, file=sys.stderr)
    # construct a new TK PhotoImage object that is 512 pixels square...
    tkPhotoImage = PhotoImage(width=s, height=s)
    # ... and use it to make a picture of a fractal
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?
    makePictureOfFractal(f[i], i, ".png", win, grad, tkPhotoImage, GREY0, None, None, s)

    if Save_As_Picture:
        # Write out the Fractal into a .gif image file
        tkPhotoImage.write(i + ".png")
        #tkPhotoImage.write(f"{i}.png")
        print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)

    if Save_As_Picture:
        # Output the Fractal into a .png image
        tkPhotoImage.write(f"{i}.png")
        print("Wrote picture " + i + ".png", file=sys.stderr)
        #tkPhotoImage.write(f"{i}.png")

    # print a message telling the user how to quit or exit the program
    print("Close the image window to exit the program", file=sys.stderr)
    # Call tkinter.mainloop so the GUI remains open
    mainloop()


## This is some weird Python thing... but all of the tutorials do it, so here we go
#if __name__ == '__main__':
#    # Process command-line arguments, allowing the user to select their fractal
#    if len(sys.argv) < 2:
#        print("Please provide the name of a fractal as an argument", file=sys.stderr)
#        for i in f:
#            print(f"\t{i}", file=sys.stderr)
#        sys.exit(1)
#
#    elif sys.argv[1] not in f:
#        print(f"ERROR: {sys.argv[1]} is not a valid fractal", file=sys.stderr)
#        print("Please choose one of the following:", file=sys.stderr)
#        for i in f:
#            print(f"\t{i}", file=sys.stderr)
#        sys.exit(1)
#
#    else:
#        fratcal_config = getFractalConfigurationDataFromFractalRepositoryDictionary(f, sys.argv[1])
#        phoenix_main(fratcal_config)



# This dictionary contains the different views of the Phoenix set you can make
# with this program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'i'.
#
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into
# this configuration dictionary instead of hardcoding it into this program.
# But I don't have time for this right now, too busy.  I'll just keep doing it
# the way I know how.
f = {
        # The full Phoneix set
        'phoenix': {
            'centerX':     0.0,
            'centerY':     0.0,
            'axisLength':  3.25,
            },

        # This one looks like a peacock's tail to me
        'peacock': {
            'centerX':     -0.363287878200906,
            'centerY':     0.381197981824009,
            'axisLength':  0.0840187115019564,
        },

        # Two or more monkeys having a scuffle
        'monkey-knife-fight': {
            'centerX':    -0.945542168674699,
            'centerY':    0.232234726688103,
            'axisLength': 0.136626506024096,
            },

        # This one makes me hungry to look at
        'shrimp-cocktail': {
            'centerX': 0.529156626506024,
            'centerY': -0.3516077170418,
            'axisLength': 0.221204819277108,
            },
        }