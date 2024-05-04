#!/bin/bash

component=$1

# Navigate into the test component directory and perform some pre-cleanup
cd ../unit-tests/$component

# /output is not removed because it is not always required to rebuild everything
# Not removing /output speeds up the feedback time, which is important for
# test driven development
rm -f test-executer
rm -rf logs; mkdir logs

# Build the test executer for this component without running the tests
# make -s all_no_tests >logs/build-log 2>logs/build-errors
make -s all_no_tests

if [ $? -eq 0 ]; then
    # Run the test executor from within the logs/junit directory
    # This places the junit xmls in /logs/junit
    mkdir -p logs/junit
    cd logs/junit
    ../../test-executer
else
    # There was a compile or link error

    # Remove the test executer, ensuring that the
    # current test-executer is always valid
    rm -f test-executer
fi
