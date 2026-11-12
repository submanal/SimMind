cmake_minimum_required(VERSION 3.18...3.28)
project(test_sim LANGUAGES CXX)

find_package(Python REQUIRED COMPONENTS Interpreter Development NumPy)

include(FetchContent)

FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v3.1.0
)
FetchContent_MakeAvailable(pybind11)

FetchContent_Declare(
    xtl
    GIT_REPOSITORY https://github.com/xtensor-stack/xtl.git
    GIT_TAG        0.8.2
)
FetchContent_MakeAvailable(xtl)

FetchContent_Declare(
    xtensor
    GIT_REPOSITORY https://github.com/xtensor-stack/xtensor.git
    GIT_TAG        0.27.2
)
FetchContent_MakeAvailable(xtensor)

FetchContent_Declare(
    xtensor-python
    GIT_REPOSITORY https://github.com/xtensor-stack/xtensor-python.git
    GIT_TAG        0.29.0
)
FetchContent_MakeAvailable(xtensor-python)

pybind11_add_module(mymodule src/module.cpp)

target_link_libraries(mymodule PRIVATE
    pybind11::module
    Python::NumPy
    xtensor
    xtensor-python
)
