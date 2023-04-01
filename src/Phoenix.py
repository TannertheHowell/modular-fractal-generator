import sys
import time
from tkinter import Tk, PhotoImage, mainloop
from ImagePainter import makePictureOfFractal
from Palette import grad, GREY0
from time import time

patternDict = {
        # The full Phoenix set
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


def phoenix_main(fractalName):
    """The main entry-point for the Phoenix fractal generator"""

    size = 512
    startTime = time()
    window = Tk()

    print("Rendering %s fractal" % fractalName, file=sys.stderr)

    tkPhotoImage = PhotoImage(width=size, height=size)
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?
    makePictureOfFractal(patternDict[fractalName], fractalName, ".png", window, grad, tkPhotoImage, GREY0, None, None, size)

    print(f"\nDone in {time() - startTime:.3f} seconds!", file=sys.stderr)
    tkPhotoImage.write(f"{fractalName}.png")
    print("Wrote picture " + fractalName + ".png", file=sys.stderr)

    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()
