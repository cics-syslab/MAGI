#!/bin/bash
# install necessary packages globally
cwd=$(pwd)
cd /autograder/source/modules/ImageProcessing/into_work_dir
npm install
cd $cwd
