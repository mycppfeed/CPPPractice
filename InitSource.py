#!/usr/bin/python3

srcCMakeContent = '''
get_filename_component(TARGET ${CMAKE_CURRENT_LIST_DIR} NAME)

add_library(${TARGET} OBJECT ${TARGET}.cpp)
target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
'''

testCMakeContent = '''
get_filename_component(TARGET_ ${CMAKE_CURRENT_LIST_DIR} NAME)
set(TARGET ${TARGET_}Test)

add_executable(${TARGET} ${TARGET}.cpp)
target_link_libraries(${TARGET} gtest_main ${TARGET_})
gtest_discover_tests(${TARGET})
'''

from os import path
from pathlib import Path
import argparse
def ParseArgs():
    parser = argparse.ArgumentParser(prog='Initialize Source Code')
    parser.add_argument('-p', '--path', dest='path', type=Path, required = True, help='Path of new source code')
    return parser.parse_args()

def InitPath(dir: Path, path: Path, cmakeContent: str):
    (dir / path).mkdir(parents = True, exist_ok = False)
    (dir / path / path.with_suffix(".cpp")).touch()
    (dir / path / "CMakeLists.txt").write_text(cmakeContent)
    with (dir / "CMakeLists.txt").open("a") as f:
        f.write("\nadd_subdirectory(" + str(path) + ")")

if __name__ == "__main__":
    args = ParseArgs()
    print("Path = {}".format(args.path))

    InitPath(Path("srcs"), args.path, srcCMakeContent)
    InitPath(Path("tests"), args.path, srcCMakeContent)
