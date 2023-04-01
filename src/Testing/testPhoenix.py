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

from Phoenix import getColorFromPalette
from Palette import grad
from FractalInformation import patternDict, getFractalConfigurationDataFromFractalRepositoryDictionary



# autocmd BufWritePost <buffer> !python3 runTests.py  	  	  

class TestPhoenix(unittest.TestCase):  	  	  
    def test_getColorFromPalette(self):  	  	  
        """Phoenix fractal configuration and algorithm output the expected colors at key locations"""  	  	  
        self.assertEqual(getColorFromPalette(complex(0, 0), grad), '#ffeca5')
        self.assertEqual(getColorFromPalette(complex(-0.751, 1.1075), grad), '#ffe4b5')
        self.assertEqual(getColorFromPalette(complex(-0.2, 1.1075), grad), '#ffe5b2')
        self.assertEqual(getColorFromPalette(complex(-0.750, 0.1075), grad), '#86ff4a')
        self.assertEqual(getColorFromPalette(complex(-0.748, -0.1075), grad), '#002277')
        self.assertEqual(getColorFromPalette(complex(-0.75625, 0.078125), grad), '#002277')
        self.assertEqual(getColorFromPalette(complex(-0.75625, -0.234375), grad), '#94ff51')
        self.assertEqual(getColorFromPalette(complex(0.33749, -0.625), grad), '#ffe7af')
        self.assertEqual(getColorFromPalette(complex(-0.678125, -0.46875), grad), '#002277')
        self.assertEqual(getColorFromPalette(complex(-0.406, -0.837), grad), '#ffe5b2')
        self.assertEqual(getColorFromPalette(complex(-0.186, -0.685), grad), '#ffe7af')

    def test_dictionaryGetter(self):  	  	  
        """Names of fractals in the configuration dictionary are as expected"""  	  	  
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(patternDict, 'absent'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(patternDict, 'phoenix'))
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(patternDict, ''))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(patternDict, 'peacock'))
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(patternDict, 'Still Not In Here'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(patternDict, 'monkey-knife-fight'))
        self.assertIsNone(getFractalConfigurationDataFromFractalRepositoryDictionary(patternDict, 'shrimp-coctail'))
        self.assertIsNotNone(getFractalConfigurationDataFromFractalRepositoryDictionary(patternDict, 'shrimp-cocktail'))

    def test_gradientLength(self):  	  	  
        """Color palette contains the expected number of colors"""  	  	  
        self.assertEqual(108, len(grad))  	  	  

    # # added this unit test that ChatGPT gave me:
    # def test_getColorFromPaletteOutOfBounds(self):
    #     """getColorFromPalette returns the default color for out-of-bounds input"""
    #     self.assertEqual(getColorFromPalette(complex(100, 100), grad), '#000000')
    #     self.assertEqual(getColorFromPalette(complex(-100, -100), grad), '#000000')


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  
