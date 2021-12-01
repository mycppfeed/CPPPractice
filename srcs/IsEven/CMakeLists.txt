get_filename_component(TARGET ${CMAKE_CURRENT_LIST_DIR} NAME)

add_library(${TARGET} OBJECT ${TARGET}.cpp)
target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
