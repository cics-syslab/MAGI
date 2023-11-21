#include <gtest/gtest.h>

extern "C" {
#include "sum.h"
}

// This class definition is required by Google Test.
// See the documentation for further details.
class EXECNAME_test : public ::testing::Test {
 protected:
  // Constructor runs before each test
  EXECNAME_test() {}
  // Destructor cleans up after tests
  virtual ~EXECNAME_test() {}
  // Sets up before each test (after constructor)
  virtual void SetUp() {}
  // Clean up after each test (before destructor)
  virtual void TearDown() {}
};

TEST(EXECNAME_test, causality_holds) {
  EXPECT_TRUE(1) << "Kudos if you can actually trigger this message\n";
  EXPECT_FALSE(0) << "Kudos if you can actually trigger this message\n";
}

TEST(EXECNAME_test, test_sum_positive) {
  int r = sum(1, 2);
  EXPECT_EQ(r, 3);
}

// PRIVATE_BEGIN
TEST(EXECNAME_test, test_sum_negative) {
  int r = sum(1, -2);
  EXPECT_EQ(r, -1);
}
// PRIVATE_END

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
