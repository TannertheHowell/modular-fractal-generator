import sys  	  	  
import time
from tkinter import Tk, Canvas, PhotoImage, mainloop


class ImagePainter:

    def __init__(self, fractal_object, color_palette, fractal_info):
        self.fractal_object = fractal_object
        self.color_palette = color_palette
        self.fractal_info = fractal_info
        self.SIZE = self.fractal_info.get("pixels")

    def paint(self):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image which is 640x640 pixels in size."""

        image_name = self.fractal_info.get('imagename')

        # Set up the GUI so that we can paint the fractal image on the screen
        print("Rendering {} fractal".format(image_name), file=sys.stderr)
        before = time.time()

        # Figure out how the boundaries of the PhotoImage relate to coordinates on
        # the imaginary plane.
        minx = self.fractal_info.get('min').get('x')
        maxx = self.fractal_info.get('max').get('x')
        miny = self.fractal_info.get('min').get('y')
        maxy = self.fractal_info.get('max').get('y')

        # Display the image on the screen
        window = Tk()
        canvas = Canvas(window, width=self.SIZE, height=self.SIZE, bg='#FDE6FA')
        canvas.pack()
        img = PhotoImage(width=self.SIZE, height=self.SIZE)
        canvas.create_image((self.SIZE/2, self.SIZE/2), image=img, state="normal")

        # At this scale, how much length and height on the imaginary plane does one
        # pixel take?
        pixelsize = self.fractal_info.get('pixelsize')

        for row in range(self.SIZE, 0, -1):
            cc = []
            for col in range(self.SIZE):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                idx = self.fractal_object.count(complex(x, y))
                color = self.color_palette.getColor(idx)
                cc.append(color)

            img.put('{' + ' '.join(cc) + '}', to=(0, self.SIZE-row))
            window.update()  # display a row of pixels
            self.progress(row)

        # Save the image as a PNG
        after = time.time()
        print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
        img.write(f"{image_name}.png")
        print(f"Wrote picture {image_name}.png", file=sys.stderr)

        # Call tkinter.mainloop so the GUI remains open
        print("Close the image window to exit the program", file=sys.stderr)
        mainloop()

    def progress(self, rows):
        portion = (self.SIZE - rows) / self.SIZE
        status_percent = '{:>4.0%}'.format(portion)
        status_bar_width = 34
        status_bar = '=' * int(status_bar_width * portion)
        status_bar = '{:<33}'.format(status_bar)
        print(''.join(list(['[', status_percent, ' ', status_bar, ']'])),
              end='\r',  # the '\r' returns the cursor to the leftmost column
              file=sys.stderr)
