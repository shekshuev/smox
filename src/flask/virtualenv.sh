#!/bin/bash
basedir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"
python3 -m venv "${basedir}/smox"
eval "${basedir}/smox/bin/pip install --upgrade pip" 
eval "${basedir}/smox/bin/pip install -r ${basedir}/requirements.txt" 
