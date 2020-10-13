#!/usr/bin/env sh

FILES_TO_PROCCESS=$(ls *.py **/*.py **/**/*.py)

isort $FILES_TO_PROCCESS
black $FILES_TO_PROCCESS -l 80
pyflakes $FILES_TO_PROCCESS