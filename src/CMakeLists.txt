cmake_minimum_required(VERSION 3.10.0)
project(test VERSION 0.1.0 LANGUAGES C CXX)

add_executable(test main.cpp)
install(TARGETS test DESTINATION bin)
# install(TARGETS myLibrary DESTINATION lib)

