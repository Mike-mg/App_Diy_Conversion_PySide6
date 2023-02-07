"""
Entry program
"""

import sys
from PySide6.QtWidgets import QMainWindow, QSlider, QApplication, QWidget, QLabel
from PySide6.QtCore import Qt, Slot, QCoreApplication


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Storage")
        self.setGeometry(800, 600)
        self.resize(0, 0)

        central_area = QWidget()
        central_area.setStyleSheet("background:  #bdcdf0")

        self.setCentralWidget(central_area)

        slider = QSlider(Qt.Horizontal, central_area)
        slider.setValue(0)
        slider.setMaximum(20)
        slider.setGeometry(320, 220, 270, 30)
        slider.valueChanged.connect(self.valueChanged)

        self.label = QLabel(central_area)
        self.label.setStyleSheet("background: yellow")
        self.label.setGeometry(300, 10, 50, 50)

        self.statusBar().showMessage("My status Bar")

        self.label.setText("test")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    @Slot(int)
    def valueChanged(self, value: int):
        self.label.setText(str(value))


app = QApplication(sys.argv)

window = Window()

window.show()
sys.exit(app.exec())
