cmake_minimum_required(VERSION 3.10.0)
project(test VERSION 0.1.0 LANGUAGES C CXX)
find_package(Eigen3 CONFIG REQUIRED)

add_executable(test main.cpp)
target_link_libraries(test PRIVATE Eigen3::Eigen)

install(TARGETS test DESTINATION bin)
# install(TARGETS myLibrary DESTINATION lib)

