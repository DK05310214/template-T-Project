if (NOT TARGET glog::glog)
    add_subdirectory(${CMAKE_SOURCE_DIR}/third_party/glog)
endif()