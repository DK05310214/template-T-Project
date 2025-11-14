cmake_minimum_required(VERSION 3.10.0)
project(cvt VERSION 0.1.0 LANGUAGES C CXX)
find_package(Eigen3 CONFIG REQUIRED)
find_package(OpenCV CONFIG REQUIRED)
message(STATUS "Opencv includes: ${OpenCV_INCLUDE_DIRS}")

add_executable(cvt main.cpp)
target_include_directories(cvt PRIVATE
    ${VCPKG_INCLUDE}
    # ${PROJECT_SOURCE_DIR}/../third_party/libheif/libheif/api
    ${PROJECT_SOURCE_DIR}/../install/include
    ${OpenCV_INCLUDE_DIRS}
)

target_link_directories(cvt PRIVATE
    ${PROJECT_SOURCE_DIR}/../install/lib
    ${VCPKG_PACKAGE_PATH}/lib
)
message(>> ${VCPKG_PACKAGE_PATH}/lib)
target_link_libraries(cvt PRIVATE Eigen3::Eigen ${OpenCV_LIBS} libheif.so libde265.a libx265.a )

install(TARGETS cvt DESTINATION bin)
# install(TARGETS myLibrary DESTINATION lib)

