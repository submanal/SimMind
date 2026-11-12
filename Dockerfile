FROM python:3.14-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    libgl1 \
    libegl1 \
    libxkbcommon-x11-0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-xinerama0 \
    libxcb-cursor0 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY CMakeLists.txt .
COPY src/ ./src/
COPY tests/ ./tests/
COPY app/ ./app/

RUN mkdir -p build && cd build && \
    cmake .. \
      -DPython_EXECUTABLE=$(which python) \
      -DNUMPY_INCLUDE_DIRS=$(python -c "import numpy; print(numpy.get_include())") && \
    cmake --build . -j$(nproc)

ENV PYTHONPATH=/app/build:$PYTHONPATH

CMD ["bash"]
