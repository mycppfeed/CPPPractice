cmake_policy(SET CMP0048 NEW)

project(CPPPractice  VERSION 1.0.0 LANGUAGES CXX)
cmake_minimum_required(VERSION 3.22)

include(cmake/GTest.cmake)
include(cmake/Sanitizers.cmake)
enable_testing()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -coverage -g -O0")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -fcoverage-mapping ")

set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -coverage")
# Exclude google_test or other generated files from coverage
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-exclude-files=_build/*")

add_subdirectory(srcs)
add_subdirectory(tests)