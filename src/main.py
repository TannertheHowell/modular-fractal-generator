#!/usr/bin/env python3

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


import sys
from ImagePainter import ImagePainter
import FractalParser
import FractalFactory
import PaletteFactory

param_count = len(sys.argv)

if param_count == 1:
    # Do the default fractal
    fractal_info = {
        'type': 'mandelbrot',
        'pixels': 640,
        'axislength': 4.0,
        'iterations': 100,
        'min': {
            'x': -2.0,
            'y': -2.0
        },
        'max': {
            'x': 2.0,
            'y': 2.0
        },
        'pixelsize': 0.00625,
        'imagename': 'mandelbrot.png'
    }
    fractal_object = FractalFactory.make_fractal(fractal_info)
    color_palette = PaletteFactory.makePalette("", fractal_info.get('pixels'))
elif param_count == 2:
    # Make the fractal specified, use default color palette
    fractal_info = FractalParser.get_frac_dic(sys.argv[1])
    fractal_object = FractalFactory.make_fractal(fractal_info)
    color_palette = PaletteFactory.makePalette("", fractal_info.get('pixels'))
elif param_count > 2:
    # Make the fractal specified, use the specified color palette
    fractal_info = FractalParser.get_frac_dic(sys.argv[1])
    fractal_object = FractalFactory.make_fractal(fractal_info)
    color_palette = PaletteFactory.makePalette(sys.argv[2], fractal_info.get('pixels'))
else:
    raise RuntimeError("Bad amount of parameters")

myImagePainter = ImagePainter(fractal_object, color_palette, fractal_info)

myImagePainter.paint()

