# Run your First Test

All commands are run from your project's root directory.

1. Create a new component
````
flubber/scripts/main.sh new-component --name=myComponent
````

This will create a directory *unit-tests/myComponent* with the minimum files
required to write and run tests.

This script also creates the *unit-tests/mocks/source* and *unit-tests/mocks/include*
directories if they do not exist, and a file called *forced_include.hpp* which
is included in all test code.

Run the tests for the new component
````
scripts/main.sh run --components=myComponent
````

You should see the following output in your terminal.

![first-test](docs/first-test.png)

The template test belongs to the *example* test group and is called *your_first_test*.
The test code is in the file *unit-tests/myComponent/tests.cpp*.
