&nbsp;
# Overview

This project assignment will help you understand: information representation, 
and bitwise operators. You
should complete all the exercises below using a text editor of your
choice.  Make sure you follow the instructions exactly.  The actual
code you write is fairly short; however, the details are quite
precise.  Programming errors often result from slight differences that
are hard to detect.  So be careful and understand exactly what the
exercises are asking you to do.

# Learning Objectives

1. Understand number conversion in different base
2. Understand bit shifting operations
3. Understand two's complement 
4. Understand overflow 

# Getting Started
To get started, follow these steps:

1. Download the [starter code](project.zip).
2. Unzip the `project.zip` with the following command `unzip -d
   PROJECT project.zip`. This will create a new directory called
   `PROJECT`. You can replace `PROJECT` with a directory name of your
   choice.
3. `cd` into the `PROJECT` directory and investigate the project.

If you follow the above steps correctly, you should have the following
folder structure after unzipping (assuming the project name is
"PROJECT"):

```
PROJECT/
  include/
  lib/
  obj/
  src/
  test/
  Makefile
```

After you have the code extracted you should go ahead and
investigate. You can run `make` from the *command line* and your
project will *build* and produce *potential* error results. See more
information below.

# Code Structure

This exercise contains the following important folders:

* **include**: This is where we keep [C/C++ header
  files](https://flaviocopes.com/c-header-files/). Header files are
  used in C/C++ to share definitions across many C/C++ source files.
* **lib**: This is where we keep any libraries that we might use. It
  will often be empty.
* **obj**: This folder is used for object files that are
  generated from the C compilation process. This folder is
  initially empty until you compile your code.
* **src**: This is the source folder where all code you are submitting
  must go. You can change anything you want in this folder (unless
  otherwise specified in the problem description and in the code we
  provide), you can add new files, etc.
* **test**: This is the test folder where you can find all of the
  public unit tests - if any are given.
* **Makefile** - this is a "build" file. This file is used to compile
  your code.

# Compiling The Code

To compile the code in this assignment you must run the following
command:

```bash
$ make
```

The `make` command will run the C++ compiler to build a program
executable and a test executable. These are
often referred to as program *binaries* in Unix/Linux terminology.

In addition, the `make` command will produce a `submission.zip` every
time you run it. The `submission.zip` file is what you upload to
Gradescope to submit your solution. See submission instructions below.

## Compiling This Project

This project will produce a couple of executables including:

* `data_app`: this is the main executable allowing you to run the
  program that you must complete successfully.
* `data_test`: this is the test executable that will run tests on the
  code your write for this exercise.

## Testing The Code

After you have successfully compiled the code using `make` you can run
the test executable. Here is an example of what it looks like to run a
test executable:

```bash
$ ./data_test
[==========] Running 2 tests from 1 test suite.
[----------] Global test environment set-up.
[----------] 2 tests from sum_test
[ RUN      ] sum_test.test_sum_positive
[       OK ] sum_test.test_sum_positive (0 ms)
[ RUN      ] sum_test.test_sum_negative
[       OK ] sum_test.test_sum_negative (0 ms)
[----------] 2 tests from sum_test (0 ms total)

[----------] Global test environment tear-down
[==========] 2 tests from 1 test suite ran. (2 ms total)
[  PASSED  ] 2 tests.
```

The tests that are provided may be a *subset* of the tests that the
autograder will run. However, it gives you a good idea if you are on
the right track.

# Suggested Reading

It will be useful to read up on [printf][printf] to get a better
understanding of how it is used and the different formatting options
that are available.  You can also look at the documentation directly
from the command line using the `man` command like so:

```bash
$ man 3 printf
```

What does the `3` mean? It indicates which "manual section" you want
to look in.  Take a look at [this][manuals] to see which section `3`
refers to as well as other manual sections that you have access to.

# Instructions

You already know how to deal with C code, so we'll make things a bit
easier for you -- _all_ of the modifications you have to do are going
to be in `src/data.c`!

In this project, you will combine your previous knowledge of linked lists with your newly learned knowledge of data representation. 

*Take a look in `include/data.h`, take note of the `Data` struct and `DataNode` struct.*

### In the `Data` struct, we use a linked list to represent data. 

### Here is an explanation for each field of `Data`:
 - base: indicate what base this `Data` representation is in, it can be from 2 to 16 to represent an integer in different bases.
 - sign: indicate whether this `Data` represents a signed or unsigned number. 1 means signed, and 0 means unsigned. **This does not represent if the number is positive or negative**
 - number\_bits: how many bits are required to represent this number in binary, in this project, it can be from 4 to 32. This field is **NOT** affected by `base`.
 - len: the length of the linked list `data`. The value of this field will always be less than or equal to number_bits.
 - data: start of the linked list that contains the data to represent the number. The most significant digit is the first node in the list, and the least significant digit is the last node.Note: **The first node contains '0' if and only if the data being represented is the number 0.**

### In the `DataNode` struct, there are two fields:
 - number: this field contains the value of this `DataNode`, this can be from 0-9 or A-F when base higher than 10 is used.
 - next: pointer to the next `DataNode`.

For example, `int 205` can be represented with the following `Data`:
 - base: 10
 - sign: 1
 - len: 3
 - number\_bits: 32
 - data: '2' -> '0' -> '5'

This example is similar to the one given in `main.c`. Note that although `number_bits` is 32, the length is not 32 and there are only 3 nodes in `data`.

That is for a decimal number, however, we can also represent a number in hexidecimal. If we were to represent `int 205` in hexdecimal, `Data` would look like this:
 - base: 16
 - sign: 1
 - len: 2
 - number\_bits: 32
 - data: 'C' -> 'D'



## Part 1: Understand The Code

We provide you with starter code for this assignment.  Your first task
is to **read through data.c and data.h** files in detail so
you understand the structure of the code.  

## Part 2: Implement A Number Conversion Function

The second part of this assignment is to write the function `convert_to_base_n` in the file `src/data.c`. This function takes in a `Data`, then convert that `Data` to the destination base `n` and return the `Data`.

## Part 3: Implement A Function to return an int Representation of A Number

The third part of this assignment is to write the function `convert_to_int` in the file
`src/data.c`. This function takes in a `Data`, and returns the number as
a standard int. You are required to apply two's complement if the input number is a negative number.

Hint: Think about how to tell if this `Data` represent a negative number.

Here are three examples of the sample input to help you understand the data structure.

#### Example 1:

base = 2, sign = 1, number\_bits = 8, len = 2, data = 1 -> 0

The corresponding decimal number is 2.

Reason: The data represented is `00000010`, however, leading zeros in the linked list should be removed.

#### Example 2:

base = 2, sign = 1, number\_bits = 8, len = 8, data = 1 -> 1 -> 1 -> 1 -> 1 -> 1 -> 1 -> 1

The corresponding decimal number is -1.

Reason: The most significant number is the sign bit.

#### Example 3:

base = 16, sign = 1, number\_bits = 8, len = 2, data = F -> F

The corresponding decimal number is -1.

Reason: FF's binary correspondence is the same as example 2.

## Part 4:  Implement A Left Shift Function

Now it is time to implement the binary operator - left shift. 
In this part, you are asked to implement the function `left_shift` in the file `src/data.c`. 
The `Data` returned from `left_shift` must be in base 2 regarding of the input base.

#### Example: 
If the input`Data` is 3 in base 10 and with 16 bits, then running left shift with N=1,
 the return data must contains the linked list: 1->1->0 in base 2.
Note that the data stored in head node cannot be '0' if the return number is not 0,
 so the linked list cannot be 0->1->1->0. In other words, leading '0' should be removed. 

## Part 5:  Implement A Right Shift Function

After completing left shift operator, the last part is to implement right shift operator.
In this part, you are asked to implement the function `riight_shift` in the file `src/data.c`.
You are asked to apply logical Shift arithmetic shift based on whether the number is signed or unsigned.
The `Data` returned from `right_shift` must be in base 2 regardless of the input base.

#### Example: 
If the input `Data` is 9 in base 16 and with 16 bits, then running right shift with N=1,
 the return data must contains the linked list: 1->0->0 in base 2.
Note that the data stored in head node cannot be '0' if the return number is not 0,
 so the linked list cannot be 0->1->0->0. 


# Debugging Help

It is important that you use the `gdb` debugger to debug your code
when you encounter problems. You can easily start the `gdb` debugger
from the command line:

```bash
$ gdb PROGRAM
```

Where `PROGRAM` is the program you compiled. You should look at the
provided `gdb` cheatsheet to see some of the commands you can
execute. If you need additional help you can take a look at [this
tutorial](https://www.cs.cmu.edu/~gilpin/tutorial/).

You will inevitably encounter cases when your code fails a test or
worse, the test program exits with a segmentation violation
(segfault). To debug the code in a test requires you to understand how
the google test framework generates C++ code and how the C++ compiler
generates method signatures. In short, this is what you want to do:

```bash
$ gdb TEST_PROGRAM
(gdb) b TestSuite_TestName_Test::TestBody()
```

The `SuiteName` and `TestName` correspond to how you write a test
using the google test framework. In particular, this is the basic
structure of a test:

```C++
TEST(SuiteName, TestName) {
  // the test body
}
```

You should also know that the `b` (break) command provides tab
completion. So, you can type in the following:

```bash
(gdb) b TestSuite[TAB][TAB]
```

The `[TAB]` is hitting the `tab` key on your keyboard. You can hit it
twice in rapid succession to see all the possible completions.

# Autograder

The autograder is used to test your code more deeply.
We have provided you with some public tests and some private tests in Gradescope. 
You will need to come up with some of your own. Try to think of all of the
 edge cases that could occur, and write tests to check for each of them.
You can use the name of the private test cases as reference to create your own tests.
You will not be graded on your tests, but writing them and passing them
 is the only way that you can be reasonably sure that your code works.

To run the autograder on your solution you must upload your
`submission.zip` file (generated by running `make`) to
Gradescope. More information about how to do this is provided below.

# General Information and Project Policies

* Read this entire document. If, after a careful reading, something
  seems ambiguous or unclear to you, then communicate to the course
  staff immediately. Start this assignment as soon as possible. Do not
  wait until the night before the assignment is due to tell us you
  don’t understand something, as our ability to help you will be
  minimal.
* For some assignments, it will be useful for you to write additional
  C++ files. Any C++ file you write that is used by your solution
  MUST be in the provided `src` directory.
* The course staff are here to help you figure out errors, but not
  solve them for you. When you submit your solution, be sure to remove
  all compilation errors from your project. Any compilation errors in
  your project will cause the autograder to fail, and you will receive
  a zero for your submission. No Exceptions!

# Academic Honesty

All work that is completed in this assignment is your own. You may
talk to other students about the problems you are to solve, however,
you may not share code in any way. What you submit **must be your own
work*.

You may not use any code that is posted on the internet. If you are
not sure it is in your best interest to contact the course staff. We
will be using software that will compare your code to other students
in the course as well as online resources. It is very easy for us to
detect similar submissions and will result in a failure for the
exercise or possibly a failure for the course. Please, do not do
this. It is important to be academically honest and submit your work
only. Please review the [UMass Academic Honesty Policy and
Procedures](https://www.umass.edu/honesty/) so you are aware of what
this means.

Copying partial or whole solutions, obtained from other students or
elsewhere, is academic dishonesty. Do not share your code with your
classmates, and do not use your classmates' code. If you are confused
about what constitutes academic dishonesty you should re-read the
course policies.  We assume you have read the course policies in
detail and by submitting this project you have provided your virtual
signature in agreement with these policies.

# Gradescope

We use Gradescope to run our autograding software and record your
grade for these assignments. You may submit this assignment as many
times as possible up to the due date. If you encounter a problem with
the autograder you should contact the course staff immediately.

# Submission

You must submit the generated `submission.zip` file that is created by
running the `make` command to Gradescope. To do this you will need to
download the `submission.zip` file from the EdLab environment to your
local machine then upload `submission.zip` to Gradescope. Gradescope
will run your submission in our autograder environment and give you a
report of what tests passed and which did not. Again, you are welcome
to submit as many times as you would like.

[manuals]: http://unix.stackexchange.com/questions/3586/what-do-the-numbers-in-a-man-page-mean
[chart]: http://www.asciitable.com
[printf]: http://www.cprogramming.com/tutorial/printf-format-strings.html
[sizeof]: http://www.programiz.com/c-programming/examples/sizeof-operator-example
[tarball-info]: http://en.wikipedia.org/wiki/Tarball
