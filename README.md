
# 🌱 Bonsai

This repository contains interpreters for **Bonsai** — a minimal language based on a limited assembly instruction set known as **Bonsai Assembly**.

Bonsai Assembly consists of five core instructions:

```
inc    // Increments a variable  
dec    // Decrements a variable  
jmp    // Jumps to the given line number  
tst    // Jumps to the next line if the variable is not zero,  
       // and to the line after the next if it is  
hlt    // Halts program execution
```

## Variable Declarations

Variables are declared in a `.data:` section located below the code. Each variable is assigned an initial integer value.


## Example Program

This simple program adds variables `x` and `y`, storing the result in `y`:

```assembly
tst x      // Check if x == 0  
jmp 4      // If x != 0, jump to line 4  
jmp 7      // If x == 0, jump to line 7  
dec x      // Decrement x  
inc y      // Increment y  
jmp 1      // Repeat from line 1  
hlt        // Terminate execution

.data:
x: 6  
y: 3
```


