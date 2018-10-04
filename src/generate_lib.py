#!/usr/bin/python3
import os
import sys

headers = ["data_store.hpp", "data_store.cpp", "SMS_MemMap_Sample_V8/SharedMemory.h"]
module_name = "boost_lib"

# Write small cmake include file for library names
def write_cmake(lib_name, lib_path):
    file_name = '../variables.cmake'
    f = open(file_name, 'w+', -1)

    f.write("set(BOOST_LIB_NAME \"{}\")\n".format(lib_name))
    f.write("set(BOOST_LIB_SRC ${{CMAKE_CURRENT_SOURCE_DIR}}/src/{})".format(lib_path))

    f.close()


def main():
    builder = Builder(headers, module_name)
    
    builder.build()
    builder.write()

    write_cmake(builder.lib_name, builder.lib_path)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        os.chdir(os.path.join(sys.argv[1], 'src'))

    from code_builder import Builder

    main()


