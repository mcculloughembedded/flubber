#include "CppUTest/TestHarness.h"
#include "CppUTestExt/MockSupport.h"

TEST_GROUP(example)
{
    void setup()
    {
    }

    void teardown()
    {
    }
};

TEST(example, your_first_test)
{
    CHECK(false);
}
