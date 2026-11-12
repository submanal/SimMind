# Simulation of animal evolution

## 📖 About

Animals search for food, expend energy, and reproduce. Offspring inherit genes with potential mutations. Simulations allow us to compare which traits and strategies help them live longer and produce more offspring.

**Why it's needed:** To study evolutionary strategies through visualization and learning of behavioral models in a controlled environment.

## 🛠 Tech stack

| Component | Purposes  |
|-----------|-----------|
| **C++ + xtensor** | Simulation core (высокая производительность) |
| **Python + pybind11** | Behavior and learning models |
| **NumPy + xtensor-python** | Exchange arrays between C++ and Python without copying |
| **PyQt6 + pyqtgraph** | Visualization |

## 🚀 Fast start (Docker)

```bash
# 1. Assemble an image
docker build -t test_sim .

# 2. Check that C++-module works
docker run --rm test_sim python -c "import numpy as np; import mymodule; print(mymodule.sum_of_sines(np.array([0.0, 1.57, 3.14])))"
# Expected output: 1.0

# 3. Run tests
docker run --rm test_sim pytest tests/
```

## GUI (Only for linux)

Docker Desktop does not provide windows on macOS/Windows. For GUI use local venv.

```bash
xhost +local:docker
docker run --rm -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix test_sim python app/gui.py
xhost -local:docker
```
## 💻 Local assembling (Without Docker)

For Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir build && cd build
cmake .. -DPython_EXECUTABLE=$(which python) \
         -DNUMPY_INCLUDE_DIRS=$(python -c "import numpy; print(numpy.get_include())")
cmake --build . -j$(nproc)
```

For Windows:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
mkdir build; cd build
cmake .. -DPython_EXECUTABLE=(Get-Command python).Source `
         -DNUMPY_INCLUDE_DIRS=(python -c "import numpy; print(numpy.get_include())")
cmake --build . --config Release
```

## Project structure

test_sim/
├── CMakeLists.txt          # C++-module assembling
├── Dockerfile              # Enviroment
├── docker-compose.yml      # Comfortable launch
├── requirements.in         # Python dependencies
├── requirements.txt        # Lock-file (generate by pip-compile)
├── src/
│   └── module.cpp          # pybind11 for C++
├── app/
│   └── gui.py              # PyQt6 interface
└── tests/
    └── test_smoke.py       # C++/Python tests
