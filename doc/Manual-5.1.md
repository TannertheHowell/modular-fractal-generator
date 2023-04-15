# Fractal Visualizer User Manual

*   This is the **user manual**, not the **programmer's manual**
    *   Keep your instructions at a user-friendly level.
*   Explain how to run the program
    *   What is the name of the main program file?
    *   What command-line arguments are needed?
*   What output does the program produce?
    *   What is shown when the program works correctly?
    *   What is shown when an error is encountered
    *   Provide examples of both!
*   This block of instructions does not belong in the finished product
    *   Delete this before turning it in

Welcome to the Fractal Visualizer User Manual! Here I will walk you through how to use this program and all the amazing
things that you can do with it!

* First, to get yourself oriented make sure that you are within the 'cs1440-assn5' folder in your shell (or if you 
saved it in another folder, go to that folder). Once you are in your project folder within the shell, check to make sure
that you have the correct files in your program (by typing 'ls' then enter into the shell) including files like "src/",
"README.md" and "instructions". Other files such as "Testing" will also be in this folder. To start to the program use
the following command structure:
  * python src/main.py FRACTAL_NAME COLOR_PALETTE
    * Using this command you can replace 'FRACTAL_NAME' with the name of the fractal you would like and 'COLOR_PALETTE' 
    with whichever color palette you would like
      * These 'FRACTAL_NAME's include:
        * phoenix
        * mandelbrot
        * julia
        * mandel-pow3
        * coral
        * fjords
        * leaf
        * Many others that are of type 'mandelbrot', 'julia' or 'mandelbrot3' or 'phoenix'
      * You can also add in other .frac files as long as you follow the correct formatting and specifications in them!
      * These color palettes are included:
        * DarkPalette (a grayscale palette)
        * ColorfulPalette (a more vibrant variation)
    * Feel free to mix and match different fractals and different color palettes!
    * If you want to see deeper iterations of the fractals you can go into their individual .frac file to and update 
    their iteration count to a value between 64 and 512!
  * To make a new fractal or to exit the program, close the image window

* Here is what good results looks like:
  * In the case of the program working correctly, the bar will hit 100%, a message will tell you how many seconds it took
  as well as the name of the image created and instructions on how to exit the program (close the image). 
    * To see the images you produced, type 'ls' into the shell and hit enter. You should see the new fractal with a name 
    like _____.png, with the correct fractal name. 
      * To open the fractal on Windows enter 'start _____.png' into the shell
      * To open the fractal on Mac or Linux enter 'open _____.png' into the shell
  * It is also possible to get a fractal you did not expect:
    * This may happen if you do not put in inputs for the 'FRACTAL_NAME' which will result in a default Julia fractal being
    produced
    * If you do not add a 'COLOR_PALETTE' from one of the options you will get the default color palette of ColorfulPalette
    being used for your fractals

* Here are some possible error messages you may see
    * If you miss both of the inputs for the fractals name and the fractal's color palette a default fractal is made.
    * "Invalid palette requested" error:
      * try the command again, double-checking spelling and that the palette is one of the palettes in use, they are
      ColorfulPalette and DarkPalette.
    * "Concrete subclass of Fractal must implement count() method" error:
      * There is an issue with the concrete Fractal subclasses not having a 'count()' method defined
    * "Line does not contain a correct format for a key value pair" error:
      * The key, value pairs in the .frac file are formatted incorrectly, either fix the formatting or try a new .frac
    * "Invalid key value of: " + key + " was given" error:
      * The .frac file has a missing or invalid type of key in it
    * "An invalid fractal type was entered" error:
      * The type of fractal listed in the .frac file is not supported or is written incorrectly
    * "File not found" error:
      * The .frac file requested was not found, please double-check the spelling or add the .frac file
    * "Missing required parameter " + param_name + " in the fractal configuration file" error:
      * One of the required parts of the parameter dictionary was missing (such as the centerX or pixel count)
    * "Missing required parameter " + param_name + " in the fractal configuration file because it is a " + raw_dict'type' + " type" error:
      * This is caused when a specific fractal type like Phoenix or Julia are missing their extra parameters like preal
    * "Bad amount of parameters" error:
      * If too many arguments are passed in on the command line, make sure to not add anything after the color palette
    * "Concrete subclass of Palette must implement getColor() method" error:
      * This is caused when the subclasses of palette are missing an implementation of the 'getColor()' method
