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
from Phoenix import patternDict as phoenixFractals
from Phoenix import phoenix_main
from Mandelbrot import patternDict as mandelbrotFractals
from Mandelbrot import mbrot_main

phoenixPatterns = []
for pattern in phoenixFractals.keys():
    phoenixPatterns.append(pattern)

mandelbrotPatterns = []
for pattern in mandelbrotFractals.keys():
    mandelbrotPatterns.append(pattern)

if len(sys.argv) < 2:  	  	  
    print("Please provide the name of a fractal as an argument")

    allPatterns = phoenixPatterns + mandelbrotPatterns
    for pattern in allPatterns:
        print("\t{}".format(pattern))
    sys.exit(1)

fractal = sys.argv[1]
if fractal in phoenixPatterns:
    phoenix_main(fractal)
elif fractal in mandelbrotPatterns:
    mbrot_main(fractal)
else:
    print("Pattern type not recognized, try another pattern type")
    sys.exit(1)
