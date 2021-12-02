#include "classes.hpp"
#include <gtest/gtest.h>

TEST(ClassTest, EmptyClass) {
    EXPECT_EQ(sizeof(EmptyClass), 1);
    EXPECT_EQ(sizeof(SimpleClass_0), 4);
}

class ClassTestFix : public ::testing::Test {
protected:
    void SetUp() override {
        simpleClass_0.x = 1;
        simpleClass_1.setX(2);
    }

    SimpleClass_0 simpleClass_0;
    SimpleClass_1 simpleClass_1;
 };


TEST_F(ClassTestFix, SimpleClass0) {
    EXPECT_EQ(true, true);
    EXPECT_EQ(sizeof(SimpleClass_0), 4);
    
    EXPECT_EQ(simpleClass_0.x, 1);
    EXPECT_EQ(simpleClass_1.getX(), 2);
}


// TEST(ClassTest, SimpleClassCheckValue) {
//     EXPECT_EQ(sizeof(SimpleClass_0), 4);
// }
