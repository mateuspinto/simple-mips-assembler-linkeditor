# ALMa - Advanced Linkeditor and MIPS Assembler TP1-OC1-UFV
![MIPS LOGO ](https://i.imgur.com/0GJpEUV.png)
ALMa is an advanced linkeditor and MIPS assembler that can turn MIPS assembly code into binary, no matter if it has function calls or not. All currently MIPS assembly functions are supported. You can use ALMa as an compiler like GCC or import it on another python project. 
# About used programming language

The present code was written in Object Oriented Python 3.

# Okay, cool, but there is no executable. How can I run this?

To avoid compatible errors, no executable was distributed with this code, but you can interpret this in your machine with Python 3.

## On Linux or MAC based distros
If you don't have Python 3 installed or you're not sure about this, open your terminal and run:
### On Ubuntu based distros
    sudo apt install python3
    
### On Arch based distros
    su
    pacman -Sy python3
After that, open your terminal, clone the rep and put the input and output filenames in the command. ALMa comes with a simple MIPS assembly file called "exemplo.asm".

    git clone https://github.com/cs-aslan/ALMa_Mips_Mounter_and_Link_Editor-TP1-OC1-UFV
    make all input=exemplo.asm output=exemplo.bin
### On Windows based systems
If you don't have Python 3 installed or you not sure about this, download it [here](https://www.python.org/downloads/windows/)

Open Windows command line and put that command. You're can substitute exemplo.asm and exemplo.bin with the input and output those you wish.

    python3 mipsMounter.py -o exemplo.bin exemplo.asm
Note that it works as well in Linux and Mac systems.
# MIPS
MIPS, or Microprocessor without interlocked pipeline stage, is an architecture based entirely on registers to perform logical arithmetic operations. The purpose of this work is to implement a subset of these instructions, in particular the 32-bit MIPS instruction set.



# About data structs and why I chose them
All the code was written using dictionaries, since ALMa is based on strings and conditional cases. 
# Complexity Analysis
Since the most expensive primary struct is a dict, the complexity is **O(logN)**.
# Who am I?
My name is **Mateus Pinto da Silva**, I'm a Brazilian redhead computer scientist (currently graduating), who loves to program in Python using Object-oriented Programming and to describe hardware in Verilog HDL. I'm a data science enthusiast, current intern of a Brazilian Enterprise called Cinnecta. I like to train models in TensorFlowAPI when I have nothing better to do, and if you check my github profile, you will see that I usually don't have nothing better to do in fact. I study on Federal University of Viçosa.


> Written with [StackEdit](https://stackedit.io/).
