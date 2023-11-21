# README OUT OF DATE

The below is copied from the 230 template,
this document needs to be updated to reflect differences and changes.

# 230 Programming Assignment Template

This is a template that should be used to create a new 230 programming
assignment. It comes with scripts that will auto generate a gradescope style
autograder and a project for the students.

# Structure

The structure of a 230 template includes a number of important directories such
as `docs`, `googletest`, `include`, `lib`, `scripts`, `src`, and `test`. In
addition, at the top level we include other important files such as
`.clang-format`, `Makefile`, `run_autograder`, `setup.sh`, and `test_list.yml`.

Here is a description of each:

* `docs` - this is where we keep the documentation of the project. To update the
  documentation you must edit `docs/index.md` using *markdown* format.
* `include` - this is where all of the include files go (e.g., .h files).
* `lib` - this is where any additional libraries should go if needed.
* `scripts` - this is where we keep scripts to automate things.
* `src` - this is where the source code solution is.
* `test` - this is where the tests are.
* `.clang-format` - this describes the required formatting and will auto-format
  the distribution.
* `Makefile` - this is how we build the project.
* `run_autograder` - this is how we run the autograder on gradescope.
* `setup.sh` - this is the requirements for the environment.
* `test_list.yml` - this is used to designate points to individual tests.

# Instructor Instructions

Do the following to create a new project repository:

1. Click on the "Use as Template" green button.
2. Choose the `umass-cs-230` organization.
3. Choose a repository name as `230-project-NAME` where `NAME` is the name of the project.

After you do this, it will create a new repository in the `umass-cs-230` organization with the name `230-project-NAME`.

Do the following to create project source code and distribution:

1. Add project source code to the `src` directory.
2. Add project tests to `test/test.cpp`.
3. Update `test_list.yml` based on the test cases stated in `test/test.cpp`
4. Test your project to make sure everything is working.
5. Run the command: `make dist`. This will generate a `docs/project.zip` file. The `docs` folder is where the website content will be published. There is a link in the template documentation to `project.zip` so do not change the name of this file. This will also create a `dist` folder that contains the student version of the code and the gradescope autograder zip file.
6. Commit all changes (naturally, you have already been committing all along, right?) and push to github.

To actually publish the project to the world, do this:

1. Write the documentation for the project in `docs/index.md`. There is a template that has been provided for you. Fill in the blanks with the most articulate language you can use - it really helps students when you are clear and concise. We all try to be, but the extra effort really goes a long way.
2. Modify `_config.yml` to include the project name and a short description (these will appear on the website for the project).
2. After you have completed the documentation (or before if you are just too excited), go into settings and enable github pages by selecting that the github pages site is to be built from the `docs` folder in the master branch. See this [documentation](https://help.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) for more details.

It may take a few minutes for github to build your site, but after some time it should be accessable at `https://umass-cs-230.github.io/project-repository-name/`, where `project-repository-name` is the name you chose when you forked the original template.

Lastly, upload the autograder to Gradescope and test on both the autograder itself (simply upload the autograder as the submission) as well as the student distribution.

Notes:

1. Make sure all of the project tests pass before deploying the project to students. Any problems you encounter with a new project should be captured as "issues" in the associated github repository.
2. Make sure you run `python3 scripts/distribute.py` every time you make a change to the source code.
