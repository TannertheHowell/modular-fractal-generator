# CS 1440 Assignment 5.0: Refactoring - Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Paste up to 10 lines of offensive code between a triple-backtick fence `` ``` ``
    *   If the block of bad code is longer than 10 lines, paste a brief, representative snippet
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!
*   At least *one instance* of each smell is required for full marks
    *   Reporting one smell multiple times does not make up for not reporting another smell
    *   Ex: reporting two global variables does not make it okay to leave spaghetti code blank

## Code Smells Report

0. **Magic** numbers `src/phoenix_fractal.py` [lines 165, 177]
    * This number is used in multiple places, but it's not a variable
    * ```python	
          area_in_pixels = 640 * 640  
        ```
    * Create a variable for the amount of pixels to make it easily modifiable in the future. 

0. **Magic** numbers `src/mbrot_fractal.py` [lines 240, 243, 245, 247, 262, 263, 266, 273, 274]
    *   This image width or height is popping up again and again and again without explicitly saying what it is for
    *   ```python	
          total_pixels = 512 * 512  # 262144  
          for row in range(512, 0, -1):
          portion = 512 - row / 512 
          portion = 512 - row / 512 # prepare for next loop 
        ```
    *   Create a variable for the height/width to make it easily modifiable in the future. 

1. **Global** variables `src/phoenix_fractal.py` [lines 69,70, 315, 316, 317]
    *   These are both global variables that really just need to be normal variables within the function
    *   ```python	
             global grad  	  	  
             global win   
             global tkPhotoImage  	  	  
             global win  	  	  
             global s    
        ```
    *   This should not be a global variable, it should just be local within the function.  

2. **Poorly-named** identifiers at `src/phoenix_fractal.py` [lines 185]
    *   r is something, honestly not even sure what it is supposed to be right now
    *   ```python
    r = s  	  
        ```
    * Figure out what r should be (pixel count?), then give it an appropriate, helpful name

3. **Bad** Comments at `src/main.py` [lines 81-113]
    *   I mean this massive 'art' piece is beyond distracting and unnecessary
    *   ```python
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
        ```
    *   Cut it out, no need for any of those comments. 

4. **Too many** arguments at `src/mbrot_fractal.py` [lines 272]
    *   This get two parameters passed in, but only one is even used
    *   ```python
  	def pixelsWrittenSoFar(rows, cols):  
        ```
    * Remove the unnecessary extra parameters

5. Function/Method that is **too long** `src/phoenix_fractal.py` [lines 272]
    *   This function has 10 parameters being passed in, it must be doing too much
    *   ```python
  	makePictureOfFractal(f[i], i, ".png", win, grad, tkPhotoImage, GREY0, None, None, s)   
        ```
    *   Break this function up into maybe two different functions that handle more specific tasks

6. **Redundant** code at `src/main.py` [lines 100, 101]
    *   'i' is a variable that is set to equal '0', but the same thing happens two lines in a row
    *   ```python
    i = 0                 ##############   #####################################  	  	  
    i = 0                   ##########     ####################################  	  
        ```
    * Remove the second 'i' (and all the comments)

7. Decision tree that is **too complex** at `src/main.py` [lines 100, 101]
    * This decision tree is over 30 lines long with a lot of places that things could go wrong, plus other issues like the
   import and globals used
    * ```python
     if palette is not None:  	  	  
        # maybe it had something to do with 'len' being an integer variable  	  	  
        # instead of a function variable.  	  	  
        # Somebody from StackOverflow suggested I do it this way  	  	  
        # IDK why, but it stopped crashing, and taht's all that matters!  	  	  
        import builtins  	  	  
        len = builtins.len  	  	  
        len = len(palette)  	  	  
        global TWO  	  	  
        for iter in range(len):  	  	  
            z = z * z + c  # Get z1, z2, ...  	  	  
            if abs(z) > TWO:  	  	  
                z = float(TWO)  	  	  
                import builtins  	  	  
                len = builtins.len  	  	  
                if iter >= len(palette):  	  	  
                    iter = len(palette) - 1  	  	  
                return palette[iter]  	  	  
            elif abs(z) < TWO:  	  	  
                continue  	  	  
            elif abs(z) > seven:  	  	  
                print("You should never see this message in production", file=sys.stderr)  	  	  
                continue  	  	  
                break  	  	  
            elif abs(z) < 0:  	  	  
                print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	  	  
                sys.exit(1)  	  	  
            else:  	  	  
                pass  	  
        ```
    * Figure out a way to cup up this decision tree into maybe two different trees or even just cut out stuff that shouldn't
   even be in it, like the globals or imports. 

8. **Spaghetti** code at `src/main.py` [lines 81]
    *   This has a strange mix of an if, not and a variable that already has a not in it leading to weird double negatives.
    *   ```python
    if not arg_is_phoneix and sysargv1_not_mndlbrt_frctl == 0:	  
        ```
    * Try to make the conditional statement more straight forward either with better variable names or a different logic tree.

9. **Dead** code at `src/mbrot_fractal.py` [lines 60, 100]
    *   This line of code has 'WHITE' getting declared but never used, same with 'MAX_ITERATIONS'
    *   ```python 
        WHITE = '#ffffff'
        MAX_ITERATIONS = 115
        ```
    * Cut them once I am sure it's not getting used or used once the code is cut up.


