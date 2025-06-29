#!/usr/bin/env bash

export CC=clang
export CXX=clang++

build_dir="build"
install_dir="install"
job_num=16
cmake_generator=""
cmake_args=()
build_args=()
clean=false
show_help=false
build_type="debug"
cmake_toolchain_file="~/local/vcpkg/scripts/buildsystems/vcpkg.cmake"

# 参数解析逻辑
while [[ $# -gt 0 ]]; do
    case "$1" in
        --target)
            build_args+=("--target" "$2")
            shift 2
            ;;
        clean)
            clean=true
            shift
            ;;
        debug)
            if [[ "$build_type" == "Release" ]]; then
                exit 1
            fi
            build_type="Debug"
            shift
            ;;
        release)
            if [[ "$build_type" == "Debug" ]]; then
                exit 1
            fi
            build_type="Release"
            shift
            ;;
        --help|-h)
            show_help=true
            shift
            ;;
        -*)
            exit 1
            ;;
        *)
            build_args+=("$1")
            shift
            ;;
    esac
done

# clean
if [[ $clean == true ]]; then
    echo "clean ${build_dir}"
    rm -rf "${build_dir:?}"
    exit 0
fi

# build
mkdir -p "${build_dir}"
cd "${build_dir}" || exit 1

if [[ -n "$build_type" ]]; then
    echo "build type: $build_type"
fi

cmake ../src . -DCMAKE_BUILD_TYPE=${build_type} -DCMAKE_TOOLCHAIN_FILE=${cmake_toolchain_file}

echo "cmake ./src ./build -DCMAKE_BUILD_TYPE=${build_type}"

cmake --build . -j${job_num}
cmake --install . --prefix=../${install_dir}