#include <gtest/gtest.h>
#include "IsEven.hpp"

TEST(ExtendedTest, IsEvenTest) {
  EXPECT_TRUE(IsEven(0));
  EXPECT_TRUE(IsEven(2));
  EXPECT_TRUE(IsEven(4));
  EXPECT_TRUE(IsEven(6));
  EXPECT_TRUE(IsEven(8));
  EXPECT_FALSE(IsEven(9));
}