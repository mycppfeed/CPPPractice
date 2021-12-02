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
    parser.add_argument('-r', '--root', dest='root', default = False, action='store_true', help='Treat as root path')
    return parser.parse_args()

def getExts(dir, is_root):
    if is_root: return []
    if dir == Path("tests"): return ["Test.cpp"]
    else: return [".cpp", ".hpp"]

def InitPath(dir: Path, args, cmakeContent: str):
    curName = args.path.name

    (dir / args.path).mkdir(parents = True, exist_ok = False)

    for ext in getExts(dir, args.root):
        (dir / args.path / (str(curName) + ext)).touch()
        if ".cpp" in ext: (dir / args.path / (str(curName) + ext)).write_text("#include \"" + curName + ".hpp\"")

    with (dir / args.path.parent / "CMakeLists.txt").open("a") as f:
        f.write("\nadd_subdirectory(" + str(curName) + ")")

    if not args.root:
        (dir / args.path / "CMakeLists.txt").write_text(cmakeContent)


if __name__ == "__main__":
    args = ParseArgs()
    print("Path = {}".format(args.path))
    print("IsRoot = {}".format(args.root))

    InitPath(Path("srcs"), args, srcCMakeContent)
    InitPath(Path("tests"), args, testCMakeContent)
