cmake_minimum_required(VERSION 3.12)
project(pcars2_python_wrapper
    DESCRIPTION "Python wrapper for Project Cars 2 shared memory implementation"
)

set(CMAKE_CXX_STANDARD 11)

add_library(pcars2_python_wrapper SHARED
    src/Store.cpp
    src/Store.h
)
