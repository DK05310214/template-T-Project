cmake_minimum_required(VERSION 3.10.0)
project(test)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# 禁用编译器特有的扩展，确保代码遵循ISO C++标准
set(CMAKE_CXX_EXTENSIONS OFF)

set(VCPKG_PACKAGE_PATH ~/local/vcpkg/installed/x64-linux)
include(ExternalProject) # 引入模块

# # # 设置三方库的安装前缀
# set(THIRD_PARTY_INSTALL_PREFIX ${PROJECT_SOURCE_DIR}/install)

# ExternalProject_Add(
#     libheif_external # 外部项目目标名
#     GIT_REPOSITORY "https://github.com/strukturag/libheif.git"
#     # GIT_TAG "v1.x" # 指定版本
#     CMAKE_ARGS 
#         -DCMAKE_INSTALL_PREFIX=${THIRD_PARTY_INSTALL_PREFIX} # 关键：指定安装位置
#         -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
#         -DSPDLOG_BUILD_SHARED=OFF # 示例选项
#     BUILD_ALWAYS OFF # 避免重复构建
#     UPDATE_DISCONNECTED ON # 可离线构建
# )
include(./cmake/spdlog.cmake)
# include(./cmake/libheif.cmake)
add_subdirectory(./src)