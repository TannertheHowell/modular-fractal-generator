import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time

from Palette import palette, grad
from Mandelbrot import PixelColorOrIndex
from Phoenix import getColorFromPalette


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
