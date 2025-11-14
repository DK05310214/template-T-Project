cmake_minimum_required(VERSION 3.10.0)
find_package(Eigen3 CONFIG REQUIRED)

add_executable(print main.cpp)
# target_include_directories(print PRIVATE ${PROJECT_SOURCE_DIR}/third_party/spdlog/include)
include_directories(${PROJECT_SOURCE_DIR}/third_party/spdlog/include)
target_link_libraries(print PRIVATE Eigen3::Eigen spdlog)

install(TARGETS print DESTINATION bin)
# install(TARGETS myLibrary DESTINATION lib)

