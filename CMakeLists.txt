cmake_minimum_required(VERSION 3.10.0)
project(test)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# 禁用编译器特有的扩展，确保代码遵循ISO C++标准
set(CMAKE_CXX_EXTENSIONS OFF)
list(APPEND CMAKE_PREFIX_PATH "${PROJECT_SOURCE_DIR}/third_party/opencv")

# include(./cmake/glog.cmake)
include(./cmake/spdlog.cmake)
add_subdirectory(./src)