import sys
import os

_build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build")
if _build_dir not in sys.path:
    sys.path.insert(0, _build_dir)

import numpy as np
import mymodule

def test_sum_of_sines():
    arr = np.array([0.0, np.pi/2, np.pi])
    assert abs(mymodule.sum_of_sines(arr) - 1.0) < 1e-9

def test_double_array():
    arr = np.array([1.0, 2.0, 3.0])
    result = mymodule.double_array(arr)
    assert np.allclose(result, [2.0, 4.0, 6.0])
