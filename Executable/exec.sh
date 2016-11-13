#!/bin/bash

SCRIPT=$(dirname "$(readlink -f "$0")")
export ROOT="$SCRIPT/"

python "${ROOT}../SourceCode/manage.py" runserver 0.0.0.0:8080
