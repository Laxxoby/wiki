# C Programming Language

**C programming language** is a general-purpose programming language developed in the 1970s by Dennis Ritchie at Bell Labs for the UNIX operating system.

## Key Features

- **Simplicity:** C is known for its simple and straightforward syntax, making code writing and understanding easy.
- **Portability:** Programs written in C are highly portable, meaning they can run on various platforms with few or no modifications.
- **Efficiency:** C allows precise control over hardware, resulting in efficient programs in terms of time and space.
- **Structured:** C supports structured programming, facilitating the organization of code into functions and logical blocks.

## Basic Syntax

### Hello World in C

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

In this example, `#include <stdio.h>` is used to include the standard input/output library. The `main` function is the program's entry point.

### Variable Declaration

```c
int age = 25;
float height = 1.75;
char letter = 'A';
```

In C, variables must be declared before use. The syntax is the data type followed by the variable name.

### Control Structures

#### Conditional - If-else

```c
int number = 10;

if (number > 0) {
    printf("The number is positive.\n");
} else {
    printf("The number is negative or zero.\n");
}
```

#### Loop - For

```c
for (int i = 0; i < 5; i++) {
    printf("Iteration %d\n", i);
}
```

## Functions

```c
#include <stdio.h>

// Function declaration
int add(int a, int b);

int main() {
    int result = add(3, 4);
    printf("The sum is: %d\n", result);
    return 0;
}

// Function definition
int add(int a, int b) {
    return a + b;
}
```

In this example, a function called `add` is declared and defined, taking two parameters and returning their sum.

The C language is widely used in operating system development, device driver creation, low-level software, and high-performance applications due to its efficiency and flexibility.