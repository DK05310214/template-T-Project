cmake_minimum_required(VERSION 3.10.0)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# 禁用编译器特有的扩展，确保代码遵循ISO C++标准
set(CMAKE_CXX_EXTENSIONS OFF)
add_subdirectory(./src)