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
  * python src/main.py FRACTAL_NAME
    * Using this command you can replace 'FRACTAL_NAME' with the name of the fractal you would like
    * If you are unsure of the different fractal types, simply type "python src/main.py", followed by the enter key to
    see a list of fractals, then use the command above, with the appropriate fractal name to get that fractal

* After running the command, with a valid fractal type, you should see a line in your shell saying "Rendering _____ fractal"
with the name of the fractal you chose. Under that you will see a loading bar progressing.
  * In the case of the program working correctly, the bar will hit 100%, a message will tell you how many seconds it took
  as well as the name of the image created and instructions on how to exit the program (close the image). 
    * To see the images you produced, type 'ls' into the shell and hit enter. You should see the new fractal with a name 
    like _____.png, with the correct fractal name. 
      * To open the fractal on Windows enter 'start _____.png' into the shell
      * To open the fractal on Mac enter 'open _____.png' into the shell
      * To open the fractal on Linux.... If you're using Linus you better already know or how did you even get to this point?
  * In the case of the program having an error:
    * If you type in the command without a fractal name: You will get a list of the possible fractals which you can then 
    use to try again with a new command
    * If you mistype a fractal name, or try one that doesn't exist you will get an error of "ERROR: ______ is not a 
    valid fractal". To fix this error, enter a valid (and correctly spelt) fractal name at the end of the command

