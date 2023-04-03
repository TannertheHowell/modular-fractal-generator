import sys  	  	  
import time  	  	  

from tkinter import Tk, Canvas, PhotoImage, mainloop
import Mandelbrot
import Phoenix
from Palette import MBROT, PHENX, BLACK


SIZE = 512

def paint(fractal, imagename):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 640x640 pixels in size."""

    # Set up the GUI so that we can paint the fractal image on the screen
    print("Rendering {} fractal".format(imagename), file=sys.stderr)
    before = time.time()

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    # Display the image on the screen
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg=BLACK)
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE/2, SIZE/2), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / SIZE

    for row in range(SIZE, 0, -1):
        cc = []
        for col in range(SIZE):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            if fractal['type'] == 'mandelbrot':
                idx = Mandelbrot.count_iterations(complex(x, y), len(MBROT))
                color = MBROT[idx]
            else:
                idx = Phoenix.count_iterations(complex(x, y), len(PHENX))
                color = PHENX[idx]
            cc.append(color)

        img.put('{' + ' '.join(cc) + '}', to=(0, SIZE-row))
        window.update()  # display a row of pixels
        progress(row)

    # Save the image as a PNG
    after = time.time()
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
    img.write(f"{imagename}.png")
    print(f"Wrote picture {imagename}.png", file=sys.stderr)

    # Call tkinter.mainloop so the GUI remains open
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()


def progress(rows):
    portion = (SIZE - rows) / SIZE
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    print(''.join(list(['[', status_percent, ' ', status_bar, ']'])),
          end='\r',  # the '\r' returns the cursor to the leftmost column
          file=sys.stderr)
