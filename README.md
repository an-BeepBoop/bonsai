# bonsai
In order to familiarize myself with various programming languages, I developed interpreters for Bonsai — a minimal language based on a limited assembly instruction set known as Bonsai Assembly.
The bonsai-assembly consists of five instructions:
```
inc : Increments a given variable (more information on variables later.
dec : Decrements a variable.
jmp : Jumps to the given line number and executes the following code from there.
tst : Jumps to the next line if the given variable is not zero and to the line after the next line if it is.
hlt : Stops program execution.
```
Variables are declared in a section under the code and are declared with the tag `"section .data:`".

A simple code example would be:
```
tst 1 //Determines if the variable 1 is zero and jumps accordingly
jmp 4 //Jumps to line 4 if variable 1 is zero
jmp 7 //Jumps to line 7 if variable 1 is zero
dec 1 //Decrements variable 1
inc 2 //Increments variable 2
jmp 1 //Jumps to line 1
hlt //Stops the program

section .data:
1: 6
2: 3
```

This simple program adds variables 1 and 2.


