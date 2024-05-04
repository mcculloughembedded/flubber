#include "CppUTest/CommandLineTestRunner.h"
#include <stdio.h>

int main(int ac, char ** av)
{
    return CommandLineTestRunner::RunAllTests(ac, av);
}
