#!/bin/bash

# https://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$DIR/lib/"
export PYTHONPATH="$PYTHONPATH:$DIR/src/py_utils/"

