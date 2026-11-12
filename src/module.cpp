#include <pybind11/pybind11.h>
#include <numeric>

#define FORCE_IMPORT_ARRAY
#include <xtensor-python/pyarray.hpp>
#include <xtensor/core/xmath.hpp>

namespace py = pybind11;

double sum_of_sines(xt::pyarray<double>& arr) {
    auto sines = xt::sin(arr);
    return std::accumulate(sines.cbegin(), sines.cend(), 0.0);
}

// Пример возврата массива в Python
xt::pyarray<double> double_array(xt::pyarray<double>& arr) {
    return arr * 2.0;
}

PYBIND11_MODULE(mymodule, m) {
    xt::import_numpy();
    m.doc() = "test_sim C++ module";
    m.def("sum_of_sines", &sum_of_sines, "Sum sin(x) over array");
    m.def("double_array", &double_array, "Multiply array by 2");
}
