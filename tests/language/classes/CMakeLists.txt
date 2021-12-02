
get_filename_component(TARGET_ ${CMAKE_CURRENT_LIST_DIR} NAME)
set(TARGET ${TARGET_}Test)

add_executable(${TARGET} ${TARGET}.cpp)
target_link_libraries(${TARGET} gtest_main ${TARGET_})
gtest_discover_tests(${TARGET})
install(TARGETS ${TARGET})