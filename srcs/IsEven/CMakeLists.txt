set(TEST_TARGET IsEven)
add_library(${TEST_TARGET} OBJECT IsEven.cpp)
target_include_directories(${TEST_TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
