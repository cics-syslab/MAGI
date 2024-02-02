# NetworkProjectEngine

This engine generates the documentation and autograder for the network project.

## Project Requirement

A successful client need to establish a connection with remote server and solve the question received from the server.

Please see the documentation in the example output for the rest details.

## Configuration

- ```QUESTION_FORMAT``` The format of the question strings shown to students.

### QA.py

- ```generateQuestion() ```
  This function need to randomly generate questions for the client to solve.

- ```solveQuestion()```
  This function will be the solver for the question. It needs to parse generated string from generateQuestion() and
  solve it. The returned answer from the client has to match the string returned in this function for tests to pass.

## TODO

- Replace the project name in the documentation, such as the occurrence of ```math bot```