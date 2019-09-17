cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

message("LIBS: ${CONAN_LIBS}")

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
if (WIN32)
        target_link_libraries(example ws2_32)
else ()
        target_link_libraries(example pthread)
endif (WIN32)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
