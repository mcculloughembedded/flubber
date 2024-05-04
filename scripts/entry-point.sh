#!/bin/bash

if [ ! -d unit-tests ]; then
  mkdir unit-tests
fi
cd unit-tests
python3 ../unit-test-executor/scripts/cmd-parser.py "$@"
