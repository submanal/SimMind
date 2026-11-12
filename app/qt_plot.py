import sys
import os

_build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build")
if _build_dir not in sys.path:
    sys.path.insert(0, _build_dir)

import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import mymodule

class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C++ -> NumPy -> pyqtgraph")
        x = np.linspace(0, 2*np.pi, 500)
        y = mymodule.double_array(x)   # C++ умножает на 2

        plot = pg.PlotWidget()
        plot.plot(x, y, pen='y')
        plot.setLabel('bottom', 'x')
        plot.setLabel('left', '2x (from C++)')
        self.setCentralWidget(plot)

app = QApplication(sys.argv)
w = PlotWindow()
w.show()
sys.exit(app.exec())
