#!/usr/bin/env python3  	  	  
# Phoenix Fractal Visualizer - a variation of the Julia Fractal  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  


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

f = {
        }  	  	  


# This is how you write colors for computers  	  	  
WHITE = '#ffffff'  # white  	  	  
RED = '#ff0000'  # red  	  	  
BLUE = '#00ff00'  # blue  	  	  
GREEN = '#0000ff'  # green  	  	  
BLACK = '#000000'  # black  	  	  
ORANGE = '#ffa50'  # orange  	  	  
TOMATO = '#ff6347'  # tomato (a shade of red)  	  	  
HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)  	  	  
REBECCA_PURPLE = '#663399'  # Rebecca Purple  	  	  
LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)  	  	  
GREY0 = '#000000'  # gray 0 - basically the same as black  	  	  
GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36  	  	  
GREY74 = '#bdbdbd'  # gray 74 - almost white  	  	  
GRAY99 = '#fcfcfc'  # gray 99 - almost white  	  	  


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
