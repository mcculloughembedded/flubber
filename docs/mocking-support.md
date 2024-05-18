# The Mocks Directory
Flubber supports mocking by reserving a folder called `/mocks` in the `/unit-tests` directory.
Within `/mocks`, the user can add and structure source files as they please.

Files in the `/mocks` directory are not automatically compiled.
To include a mock in a test component, add the path to the mock source files in the [test component's makefile](/test-components#structure-of-a-test-component).

# Forced Include
A file named _forced_include.hpp_ can be present in the `/unit-tests/` directory.
This file in included in all tests.

The forced include file can be used to override architecture specific pragmas.

# NDEBUG
Test components are compiled with the `NDEBUG` define.
This allows the user to include or exclude code based on whether the build is a test or production build.

The most common use case for this is to test the state of memory mapped registers on embbedded systems.
Compiling the production code off target without excluding memory mapped registers would result in pointers pointing to illegal memory in the test executable.
To test the state of a memory mapped register, the `NDEBUG` flag can be used to exclude the production definition of the registers, and instead allocate memory on the test architecture.
