cmake_minimum_required (VERSION 3.12)
project (boost_test 
    DESCRIPTION "Boost Project Cars2 shared memory wrapper"
    LANGUAGES CXX
)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Includes
find_package(PythonInterp 3.7 REQUIRED)
find_package(PythonLibs 3.7 REQUIRED)

include_directories(PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src ${PYTHON_INCLUDE_DIRS} ${Boost_INCLUDE_DIR})
link_directories(${BOOST_LIBRARY_DIR})

add_custom_command(
    COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/src/generate_lib.py ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/src/generate_lib.py
    OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/src/module/boost_lib.cpp
    COMMENT "Generating boost"
)

include(boost_lib_variables.cmake)

# Create library from store class
add_library(store_lib SHARED src/data_store/data_store.cpp)

# Create actual boost library
add_library(boost_lib SHARED ${CMAKE_CURRENT_SOURCE_DIR}/src/module/boost_lib.cpp)
target_link_libraries(boost_lib boost_python3)

# Prefix and output dir settings
set_target_properties(boost_lib PROPERTIES PREFIX "")
set_target_properties(store_lib PROPERTIES PREFIX "")

add_custom_command(TARGET boost_lib 
    POST_BUILD 
    COMMAND ${CMAKE_COMMAND} -E copy
    boost_lib.so ${CMAKE_CURRENT_LIST_DIR}/src/boost_lib.so
)