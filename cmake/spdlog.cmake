if (NOT TARGET glog::glog)
    SET(SPDLOG_INSTALL FALSE) 
    add_subdirectory(${CMAKE_SOURCE_DIR}/third_party/spdlog)
endif()