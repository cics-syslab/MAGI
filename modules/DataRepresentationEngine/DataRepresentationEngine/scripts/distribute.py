# This script generates a student distribution of the project
# from the solution + autograder version of the project.
import json
import os
import pathlib
import shutil
import textwrap
import glob
import re
import io

class DistributionCreator:
    def __init__(self, config_file):
        self.dist_name = "project"
        self.dist_path = pathlib.Path("dist") / self.dist_name
        self.dist_path_gs = pathlib.Path("dist") / "gradescope"

    # (1) Remove the student_distribution folder (maybe the name of the project)
    #  - read config.json
    #  - use the "distribution_name" field to produce folder: dist/<distribution_name>
    # (2) Create the student_distribution folder (maybe the name of the project)
    def create_distribution_folder(self):
        if os.path.exists("dist"):
            shutil.rmtree("dist")
        self.dist_path.mkdir(parents=True)
        self.dist_path_gs.mkdir(parents=True)

    # (3) Copy all files/directories into the distribution folder
    #     - lib
    #     - src
    #     - test
    #     - docs
    #     - .vscode, .classpath, .settings
    def copy_project_material(self):
        src = pathlib.Path("lib")
        shutil.copytree(src, self.dist_path / "lib")
        shutil.copytree(src, self.dist_path_gs / "lib")

        src = pathlib.Path("src")
        shutil.copytree(src, self.dist_path / "src")
        shutil.copytree(src, self.dist_path_gs / "src")

        src = pathlib.Path("include")
        shutil.copytree(src, self.dist_path / "include")
        shutil.copytree(src, self.dist_path_gs / "include")

        src = pathlib.Path("test")
        shutil.copytree(src, self.dist_path / "test")
        shutil.copytree(src, self.dist_path_gs / "test")

        src = pathlib.Path("obj")
        shutil.copytree(src, self.dist_path / "obj")
        shutil.copytree(src, self.dist_path_gs / "obj")

        src = pathlib.Path("scripts")
        shutil.copytree(src, self.dist_path_gs / "scripts")

        shutil.copy2("run_autograder", self.dist_path_gs / "run_autograder")
        shutil.copy2("setup.sh", self.dist_path_gs / "setup.sh")
        shutil.copy2("test_list.yml", self.dist_path_gs / "test_list.yml")

        shutil.copy2("Makefile", self.dist_path / "Makefile")
        shutil.copy2("Makefile", self.dist_path_gs / "Makefile")

    # (4) Remove unwanted files/folders
    def clean(self):
        os.remove(self.dist_path / "lib" / ".gitkeep")
        os.remove(self.dist_path_gs / "lib" / ".gitkeep")
        os.remove(self.dist_path / "obj" / ".gitkeep")
        os.remove(self.dist_path_gs / "obj" / ".gitkeep")

    # (5) Process all C/CPP files to remove private delineated code and uncomment
    #     student provided code
    def process(self):
        private_start_re = ".*(//|#).*PRIVATE_BEGIN.*"
        private_end_re = ".*(//|#).*PRIVATE_END.*"
        public_begin_re = ".*/\* PUBLIC_BEGIN.*"
        public_end_re = ".*PUBLIC_END.*\*/.*"

        # Controls printing output.
        flag = True

        src = self.dist_path / "src" / "**" / "*.c"
        files = glob.glob(f"{src}", recursive=True)
        tst = self.dist_path / "test" / "**" / "*.cpp"
        files.extend(glob.glob(f"{tst}", recursive=True))
        icl = self.dist_path / "include" / "**" / "*.h"
        files.extend(glob.glob(f"{icl}", recursive=True))
        makefile = self.dist_path / "Makefile"
        files.extend(glob.glob(f"{makefile}", recursive=True))
        for file in files:
            # Output buffer to collect output.
            output = io.StringIO()

            with open(file, "r") as f:
                for line in f:
                    if re.match(private_start_re, line):
                        flag = False
                    elif re.match(private_end_re, line):
                        flag = True
                    elif re.match(public_begin_re, line):
                        # We just continue, but do not produce output
                        pass
                    elif re.match(public_end_re, line):
                        # We just continue, but do not produce output
                        pass
                    elif flag == True:
                        output.write(line)

            with open(file, "w") as f:
                f.write(output.getvalue())

            output.close()

    # (6) Package distribution
    def package(self):
        # This packages the student distribution and publishes to the website.
        docs_dir = pathlib.Path("docs")
        if os.path.exists(docs_dir / "project.zip"):
            os.remove(docs_dir / "project.zip")
        shutil.make_archive("project", "zip", self.dist_path)
        shutil.move("project.zip", docs_dir)

        # This packages the gradescope distribution
        dist_dir = pathlib.Path("dist")
        shutil.make_archive("gradescope", "zip", dist_dir / "gradescope")
        shutil.move("gradescope.zip", dist_dir)

    def run(self):
        self.create_distribution_folder()
        self.copy_project_material()
        self.clean()
        self.process()
        self.package()

if __name__ == "__main__":
    dc = DistributionCreator("config.json")
    dc.run()
