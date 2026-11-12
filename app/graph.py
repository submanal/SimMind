import sys
import os

_build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build")
if _build_dir not in sys.path:
    sys.path.insert(0, _build_dir)

import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pyqtgraph as pg
import mymodule

class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C++ -> NumPy -> pyqtgraph")
        
        # Данные из C++ (или сгенерированные в Python и обработанные C++)
        x = np.linspace(0, 2*np.pi, 500)
        y = mymodule.double_array(x)  # C++ умножает на 2
        
        plot_widget = pg.PlotWidget()
        plot_widget.plot(x, y, pen='y')
        plot_widget.setLabel('bottom', 'x')
        plot_widget.setLabel('left', '2x (from C++)')
        
        self.setCentralWidget(plot_widget)

app = QApplication(sys.argv)
window = PlotWindow()
window.show()
sys.exit(app.exec())
