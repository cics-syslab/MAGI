&nbsp;
# Quick links for this challenge

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [How big is this challenge?](#how-big-is-this-challenge)
- [TODO: Requirements](#requirements)
- [Tips / Specific Points](#tipsspecific-points)

# Quick links to reference sections

These tend not to vary much from challenge to challenge.

- [Getting Started](#getting-started) - downloading, unzipping, etc.
- [Code Structure](#code-structure) - `src`, `include`, etc.
- [Compiling The Code](#compiling-the-code)
- [Testing The Code](#testing-the-code)
- [Autograder](#autograder)
- [General Information and Project Policies](#general-information-and-project-policies)
- [Academic Honesty](#academic-honesty)
- [Gradescope](#gradescope)
- [Submission](#submission)

# Overview

A brief paragraph overview of the project.

# Learning Objectives

1. Learning objective 1
2. Learning objective 2
3. Learning objective 3
4. Learning objective 4

# How big is this challenge?

A brief paragraph articulating how much work the assignment entails.

# Getting Started

To get started, follow these steps:

1. Download the [starter code](project-PROJNAME.zip).
2. Unzip the `project-PROJNAME.zip` with the following command `unzip -d PROJECT
   project-PROJNAME.zip`. This will create a new directory called
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

* **include**: This is where we keep [C header
  files](https://flaviocopes.com/c-header-files/). Header files are
  used in C to share definitions across many C source files.
  - ***sum.h***: This is the header file that contains the
    function prototypes for functions you need to implement.
    In this challenge, you will need to ...
* **lib**: This is where we keep any libraries that we might use. It
  will often be empty.
* **obj**: This folder is used for [object files](t.ly/LiKq) that are
  generated from the C compilation process. This folder is
  initially empty until you compile your code.
* **src**: This is the source folder where all code you are submitting
  must go. You can change anything you want in this folder (unless
  otherwise specified in the problem description and in the code we
  provide), you can add new files, etc.
  - ***sum.c***: This file is the heart of the assignment.
    Most of the the work you need to do is here.
  - ***main.c***: This file contains a main function.
    This exists purely for your use, use it as you wish for casual testing and debugging.
    This file starts out containing some very simple "casual tests".
* **test**: This is the test folder where you can find all of the
  public unit tests - if any are given.
  - ***test.cpp***: This file contains all the public google tests.
    Technically, this file is written in C++, but you can edit it as though it were C,
    since the content of this class is fundamental enough to largely be in the intersection
    of C and C++.
    This exists for your use, use it as you wish for more formal/automated testing.
* **Makefile** - this is a "build" file. This file is used to compile
  your code. You are welcome to look at the inside of this file at
  any time.

# Compiling The Code

To compile the code in this assignment you must run the following
command:

```bash
$ make
```

The `make` command will run the C compiler to build a program
[executable](t.ly/hdB2) and a test [executable](t.ly/hdB2). These are
often referred to as program *binaries* in Unix/Linux terminology.

In addition, the `make` command will produce a `submission-PROJNAME.zip` every
time you run it. The `submission-PROJNAME.zip` file is what you upload to
Gradescope to submit your solution. See submission instructions below.

## Compiling This Project

This project will produce a couple of executables including:

* `EXECNAME_app`: this is the main executable allowing you to run the
  program that you must complete successfully.
* `EXECNAME_test`: this is the test executable that will run tests on the
  code your write for this exercise.
  
## Testing The Code

After you have successfully compiled the code using `make` you can run
the test executable. Here is an example of what it looks like to run a
test executable:

```bash
$ ./hello_sum_test
[==========] Running 3 tests from 1 test suite.
[----------] Global test environment set-up.
[----------] 3 tests from hello_sum_test
[ RUN      ] hello_sum_test.causality_holds
[       OK ] hello_sum_test.causality_holds (0 ms)
[ RUN      ] hello_sum_test.test_sum_positive
[       OK ] hello_sum_test.test_sum_positive (0 ms)
[ RUN      ] hello_sum_test.test_sum_negative
[       OK ] hello_sum_test.test_sum_negative (0 ms)
[----------] 3 tests from hello_sum_test (0 ms total)

[----------] Global test environment tear-down
[==========] 3 tests from 1 test suite ran. (0 ms total)
[  PASSED  ] 3 tests.
```

The tests that are provided are a *subset* of the tests that the
autograder will run. However, it gives you a good idea if you are on
the right track.

# TODO

## Requirements

High level statement about requirements

### 1. Requirement 1 ###

More detailed statement about requirement 1.

### 2. Requirement 2 ###

More detailed statement about requirement 1.

### 3. Requirement 3 ###

More detailed statement about requirement 1.

## Tips/Specific Points

As always, make use of main to test/debug. We have provided some tests for you.

Any useful tips or comments about specific things that would be helpful to students.

# Autograder

The autograder is used to test your code more deeply. If you follow
the specifications of this exercise exactly then you should be able to
pass all of the tests that you are provided and all of the tests the
autograder is using to check your solution.

To run the autograder on your solution you must upload your
`submission-PROJNAME.zip` file (generated by running `make`) to
Gradescope. More information about how to do this is provided below.

# General Information and Project Policies

* Read this entire document. If, after a careful reading, something
  seems ambiguous or unclear to you, then communicate to the course
  staff immediately. Start this assignment as soon as possible. Do not
  wait until the night before the assignment is due to tell us you
  don’t understand something, as our ability to help you will be
  minimal.
* For some assignments, it will be useful for you to write additional
  C files. Any C file you write that is used by your solution
  MUST be in the provided `src` directory.
* The course staff are here to help you figure out errors, but not
  solve them for you. When you submit your solution, be sure to remove
  all compilation errors from your project. Any compilation errors in
  your project will cause the autograder to fail, and you will receive
  a zero for your submission. No Exceptions!
* **Reminder**:

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

You must submit the generated `submission-PROJNAME.zip` file that is created by
running the `make` command to Gradescope. To do this you will need to
download the `submission-PROJNAME.zip` file from the EdLab environment to your
local machine then upload `submission-PROJNAME.zip` to Gradescope. Gradescope
will run your submission in our autograder environment and give you a
report of what tests passed and which did not. You are welcome to
submit as many times as you would like.
