set(TEST_TARGET IsEvenTest)
add_executable(${TEST_TARGET} IsEvenTest.cpp)
target_link_libraries(${TEST_TARGET} gtest_main IsEven)
gtest_discover_tests(${TEST_TARGET})
