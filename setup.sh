#!/bin/bash

# Python Setup
pip3 install --upgrade pip -q && 
pip3 install virtualenv -q && 
VENV=~/venv-dbt-and-redshift 
virtualenv $VENV -q && 
source $VENV/bin/activate && 
pip3 install --upgrade pip -q && 
pip3 install -r requirements.txt -q && 
python main.py
