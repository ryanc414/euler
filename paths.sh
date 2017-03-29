#!/bin/bash

CODEBASE_ROOT=$(dirname "$0")

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"$(pwd)/lib/"
export PYTHONPATH=$PYTHONPATH:"$CODEBASE_ROOT/src/py_utils/"

