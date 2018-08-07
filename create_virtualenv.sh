#!/bin/bash
cd  $(pwd)/requirements/ &> /dev/null
python -m virtualenv ~/virtualenv/venv-testing
source ~/virtualenv/venv-testing/bin/activate
pip install -r requirements.txt
cd ../../ &> /dev/null 