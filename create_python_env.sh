#!/bin/bash

python -m venv ENV
pip install pip --upgrade
pip install pip --use-deprecated=legacy-resolver -r requirements.txt