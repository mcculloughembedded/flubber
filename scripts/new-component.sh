#!/bin/bash

component=$1
component_dir=../unit-tests/$component

# Check if the requested component already exists
if [ -d $component_dir ]; then
  echo Component already exists!
  exit
fi

mkdir -p ../unit-tests/mocks/source
mkdir -p ../unit-tests/mocks/include

touch ../unit-tests/forced_include.hpp

mkdir -p $component_dir
cp ../unit-test-executor/templates/main.cpp $component_dir/main.cpp
cp ../unit-test-executor/templates/Makefile $component_dir/Makefile
cp ../unit-test-executor/templates/tests.cpp $component_dir/tests.cpp

sed -i "s/component-name/$component/" $component_dir/Makefile
