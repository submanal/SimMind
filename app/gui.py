import sys
import os

_build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "build")
if _build_dir not in sys.path:
    sys.path.insert(0, _build_dir)

import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import mymodule

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test_sim")
        arr = np.array([0.0, np.pi/2, np.pi])
        result = mymodule.sum_of_sines(arr)
        self.setCentralWidget(QLabel(f"sum_of_sines from C++: {result}"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
