#!/bin/bash

python3 --version
python3 -m venv app-venv
source app-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py

