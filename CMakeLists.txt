project(CPPPractice LANGUAGES CXX)
cmake_minimum_required(VERSION 3.22)

include(cmake/GTest.cmake)
include(cmake/Sanitizers.cmake)
enable_testing()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage -g -O0")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping ")

# Exclude google_test or other generated files from coverage
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-exclude-files=_build/*")

add_subdirectory(srcs)
add_subdirectory(tests)