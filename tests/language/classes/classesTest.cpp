#include "classes.hpp"
#include <gtest/gtest.h>

TEST(ClassTest, EmptyClass) {
    EXPECT_EQ(sizeof(EmptyClass), 1);
    EXPECT_EQ(sizeof(SimpleClass_0), 4);
}

class ClassTestFix : public ::testing::Test {
protected:
    SimpleClass_0 simpleClass_0;
    SimpleClass_1 simpleClass_1;
 };


TEST_F(ClassTestFix, SimpleClass0) {
    EXPECT_EQ(true, true);
    EXPECT_EQ(sizeof(SimpleClass_0), 4);
    
    EXPECT_EQ(simpleClass_0.x, 0);
    EXPECT_EQ(simpleClass_1.getX(), 0);
    EXPECT_EQ(simpleClass_1.setX(1), 0);
    EXPECT_EQ(simpleClass_1.getX(), 1);
}
