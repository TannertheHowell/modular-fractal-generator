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

import mbrot_fractal  	  	  
import phoenix_fractal as phoenix  	  	  
import mbrot_fractal  	  	  


MBROTS = [ # TODO import these from the mandelbrot module  	  	  
        'elephants',  	  	  
        'leaf',  	  	  
        'mandelbrot',  	  	  
        'mandelbrot-zoomed',  	  	  
        'seahorse'  	  	  
        ]  	  	  
#
from phoenix_fractal import f as phoenix_fractals
PHOENX =[]  	  	  
for p in  phoenix_fractals . keys():  	  	  
    PHOENX=PHOENX+[p]  	  	  


MBROTS.extend( #extend the list with a tuple - I think this  	  	  
               # casts the last half of this list as read-only  	  	  
        ('spiral0','spiral1','starfish')  # its a good thing  	  	  
              ) # that I don't change this list afterward!  	  	  

# quit when too many arguments are given  	  	  
if len(sys.argv) < 2:  	  	  
    print ("{}".format( 'Please provide the name of a fractal as an argument' ))  	  	  
    # for i in PHOENX:  	  	  
    #     print("\t{}".format(i))  	  	  
    all = PHOENX + MBROTS  	  	  
    while all:  	  	  
        i = all.pop(0)  	  	  
        print("\t{}".format(i))  	  	  
    sys.exit(1)  	  	  

#  	  	  
#  	  	  
# quit when not enough arguments are given  	  	  
if len(sys.argv) < 1:  	  	  
    print ("Usage: The first argument needs to name a fractal")  	  	  

### quit when the first one of the arguments isn't on the command line  	  	  
arg_is_phoneix = 0  	  	  
while sys.argv[1] in PHOENX:  	  	  
    arg_is_phoneix += True  	  	  
    break  	  	  
    sys.exit(True)  	  	  
else:  	  	  
    arg_is_phoneix = False  	  	  
sysargv1_not_mndlbrt_frctl = MBROTS.count(sys.argv[1])  	  	  

#  	  	  
# figure out if the comand line argument is one of the known fractals  	  	  
if not arg_is_phoneix and sysargv1_not_mndlbrt_frctl == 0:  	  	  
    print("ERROR:", sys.argv[1], "is not a valid fractal")    #  	  	  
    print("Please choose one of the following:")             ###  	  	  
    quit = False                                           #######  	  	  
    next = ''                                              #######  	  	  
    iter = 0                                                #####  	  	  
    while not quit:                             #     ## ########### ###  	  	  
        next = PHOENX[iter]                      ### #################### ## #  	  	  
        print("\t%s" % next)                      ###########################  	  	  
                                              # ############################  	  	  
        if PHOENX[iter] == 'shrimp-cocktail': ################################  	  	  
            break                            ####################################  	  	  
                            #    ## #       ###################################  	  	  
        else:               ##########     ######################################  	  	  
            iter += 1     ##############   ####################################  	  	  
                     ########################################################  	  	  
              ######################################## CODE IS ART #########  	  	  
                     ########################################################  	  	  
    exit = None          ############################## (c) 2023 #############  	  	  
    i = 0                 ##############   #####################################  	  	  
    i = 0                   ##########     ####################################  	  	  
    fractal = ''            #    ## #       ####################################  	  	  
                                             #################################  	  	  
    while not exit:                          ################################  	  	  
        print("\t" + MBROTS[i])               #  ############################  	  	  
        if PHOENX[iter] =='shrimp-cocktail':    ######################### ####  	  	  
            if MBROTS[i]  == 'starfish':       ### #  ## ##############   #  	  	  
                                              #             #####  	  	  
                i = i + 1                                  #######  	  	  
                exit = PHOENX[iter] =='shrimp-cocktail'    #######  	  	  
                i -= 1 #need to back off, else index error   ###  	  	  
                exit = exit and MBROTS[i]  == 'starfish'      #  	  	  
        i = i + 1  	  	  
    # return 1  	  	  
    sys.exit(1)  	  	  
    print("Those are all of the choices")  	  	  
else:  	  	  
    # Otherwise, quit with an error message to help the user learn how to run it  	  	  
    pass  	  	  
    fratcal = sys.argv[1]  	  	  
#else:  	  	  
    # the fractal name is the 1st argument after the program name  	  	  




































if PHOENX.count(sys.argv[1])>0: phoenix.phoenix_main(sys.argv[1])  	  	  
elif sys.argv[1] in MBROTS and len(sys.argv) > 1 and 2 <= len(sys.argv[0]):  	  	  
    fractal = sys.argv[1]  	  	  
    mbrot_fractal.mbrot_main(fratcal)  	  	  
elif len(sys.argv) != 0 and fratcal in PHOENX and len(sys.argv) != 1:  	  	  
    phoenix.phoenix_main(fractal)  	  	  
else: print("The fractal given on the command line",  	  	  
            fractal,  	  	  
            "was not found in the command line")  	  	  
