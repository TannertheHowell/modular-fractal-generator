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


import unittest  	  	  
from mbrot_fractal import PixelColorOrIndex, palette, MAX_ITERATIONS, pixelsWrittenSoFar  	  	  


# autocmd BufWritePost <buffer> !python3 runTests.py  	  	  

class TestMandelbrot(unittest.TestCase):  	  	  
    def test_pixelColorOrIndex(self):  	  	  
        """Mandelbrot fractal configuration and algorithm output the expected colors at key locations"""  	  	  
        # test the pixel color...
        self.assertEqual(PixelColorOrIndex(complex(0, 0), palette), '#7D387D')  	  	  
        self.assertEqual(PixelColorOrIndex(complex(-0.751, 1.1075), palette), '#E0DC9C')  	  	  
        self.assertEqual(PixelColorOrIndex(complex(-0.2, 1.1075), palette), '#CDDC93')  	  	  
        self.assertEqual(PixelColorOrIndex(complex(-0.75, 0.1075), palette), '#79D078')  	  	  
        self.assertEqual(PixelColorOrIndex(complex(-0.748, 0.1075), palette), '#59C0BD')  	  	  
        self.assertEqual(PixelColorOrIndex(complex(-0.7562500000000001, 0.078125), palette), '#6ECB8A')  	  	  

        # ...or Index
        self.assertEqual(12, PixelColorOrIndex(complex(-0.7562500000000001, -0.234375), None))  	  	  
        self.assertEqual(10, PixelColorOrIndex(complex(0.3374999999999999, -0.625), None))  	  	  
        self.assertEqual(29, PixelColorOrIndex(complex(-0.6781250000000001, -0.46875), None))  	  	  
        self.assertEqual(4,  PixelColorOrIndex(complex(0.4937499999999999, -0.234375), None))  	  	  
        self.assertEqual(22, PixelColorOrIndex(complex(0.3374999999999999, 0.546875), None))  	  	  

    def test_pixelsWrittenSoFar(self):  	  	  
        """Progress bar produces correct output"""  	  	  
        self.assertEqual(pixelsWrittenSoFar(1, 600), '[100% =================================]')  	  	  
        self.assertEqual(pixelsWrittenSoFar(7, 7), '[ 99% =================================]')  	  	  
        self.assertEqual(pixelsWrittenSoFar(257, 321), '[ 50% ================                 ]')  	  	  
        self.assertEqual(pixelsWrittenSoFar(256, 256), '[ 50% =================                ]')  	  	  
        self.assertEqual(pixelsWrittenSoFar(100, 100), '[ 80% ===========================      ]')  	  	  
        self.assertEqual(pixelsWrittenSoFar(640, 480), '[-25%                                  ]')  	  	  
        self.assertEqual(pixelsWrittenSoFar(137, 1000), '[ 73% ========================         ]')  	  	  
        self.assertEqual(pixelsWrittenSoFar(512, 0), '[  0%                                  ]')  	  	  

    def test_palleteLength(self):  	  	  
        """Palette contains the expected number of colors"""  	  	  
        self.assertEqual(111, len(palette))  	  	  


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
