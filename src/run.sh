#!/bin/bash

# First line - checks if Python exists on your computer
# Second line - creates a virtual environment in which the app will run
# Third line - activates the virtual environment
# Fourth line - installs the necessary python packages for you
# Fifth line - clears the terminal of the install information
# Sixth line - this runs the program

# PLEASE REFER TO README FILE FOR INSTALLATION INFORMATION

python3 --version
python3 -m venv app-venv
source app-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py

