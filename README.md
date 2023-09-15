# MAGI - Modular Assignment Generator & Inspector

A python framework for generating programming assignments and autograders for Gradescope, with extensible modules and plugins.

## Setup

1. Clone this repo
   `git clone https://github.com/cics-syslab/MAGI.git`
2. Setup the environment
   - Install the requirements with pip, the python version should be 3.10 or above. 
     ```
     pip install -r requirements.txt
     ```

## Usage
To start the Graphical User Interface, simply do ```python main.py```

The interface is divided by tabs. By default, you have two tabs, `Preview` and `BasicSettings`. After enabling different
modules or plugins, their settings (if they have) will be shown in the new tab created.

### Upload the autograder to Gradescope

In gradescope, you need to select Ubuntu 22.04

### Preview

On the preview page, you can choose where to generate the project files and generate it. (more features to come)

The files will be generated to the path and in the folder with the name as the project name. If the folder already
exists, the new folder will be concated with current time.

#### File Structure

The file structure emulates the gradescope environment under the subdirectory.

- autograder.zip

  This is the file to choose when uploading to gradescope. When selecting Base Image, please choose Ubuntu 22.04.

- source/

  Has the same contents as `autograder.zip`

- documents.md

  A document file that provides the instructions for student

- starter.zip (not implemented yet)

  starter code that needs to be provided to student

### Basic Settings

This page includes the generic information about the assignment and overall settings. The attributes are listed below,

    - Project Name: 
    The title for the project and also the name shown on the generated material such as the documentation.

    - Project Desc: 
    Optional. A paragraph long brief description for the project. Could be a scenario or something related.

    - Submission Files: 
    A list of file required for submission. In case of the student's submission doesn't include one or more files in the list, the autograder will not run or produce the test result but throws an error message to notify the student.

    - Enabled Module: 
    The module to use. Since the modules are mutually exclusive, you can only enable one module at a time.

    - Enabled Plugins: 
    The plugins to use. Multiple plugins could be enabled.

## Modules

Currently, following modules are available:

1. [Network Project Engine](https://github.com/nightdawnex/gsgen/tree/main/modules/NetworkProjectEngine)

   some description

2. [Thread Project Engine](https://github.com/nightdawnex/gsgen/tree/main/modules/ThreadingProjectEngine)

   some description

## Plugins

Currently, following plugins are available:

1. None

   some description
