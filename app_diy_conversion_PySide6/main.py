"""
Entry program
"""

import sys
from PySide6.QtWidgets import QMainWindow, QSlider, QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt, Slot # noqa


class Window(QMainWindow):

    value_percent_aroma = 0

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diy Conversion")
        self.setFixedSize(550, 650)
        self.setStyleSheet("background: #bdcdf0")

        self.central_area = QWidget()

        self.label_percent_dosage = QLabel(self.central_area)
        self.label_percent_dosage.setText("Percent Dosage Aroma")
        self.label_percent_dosage.setGeometry(175, 25, 175, 25)

        self.label_quantity_total = QLabel(self.central_area)
        self.label_quantity_total.setText("Quantity Total")
        self.label_quantity_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_quantity_total.setStyleSheet("border: 1px ridge white")
        self.label_quantity_total.setGeometry(175, 100, 175, 25)

        self.entry_quantity_total = QLineEdit(self.central_area)
        self.entry_quantity_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_quantity_total.setStyleSheet("border: 1px ridge white")
        self.entry_quantity_total.setGeometry(175, 135, 100, 25)

        self.button = QPushButton("Button", self.central_area)
        self.button.setGeometry(375, 100, 50, 25)
        self.button.clicked.connect(self.def_button)

        self.label_aroma = QLabel(self.central_area)
        self.label_aroma.setText("Dodage Aroma")
        self.label_aroma.setStyleSheet("border: 1px ridge white")
        self.label_aroma.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_aroma.setGeometry(175, 200, 175, 25)

        self.entry_aroma = QLineEdit(self.central_area)
        self.entry_aroma.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_aroma.setStyleSheet("border: 1px ridge white")
        self.entry_aroma.setGeometry(175, 235, 100, 25)

        self.button_aroma = QPushButton("Button", self.central_area)
        self.button_aroma.setGeometry(375, 100, 50, 25)
        self.button_aroma.clicked.connect(self.def_button)

        self.label_base = QLabel(self.central_area)
        self.label_base.setText("Dosage Base")
        self.label_base.setStyleSheet("border: 1px ridge white")
        self.label_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_base.setGeometry(175, 300, 175, 25)

        self.entry_base = QLineEdit(self.central_area)
        self.entry_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_base.setStyleSheet("border: 1px ridge white")
        self.entry_base.setGeometry(175, 335, 100, 25)

        self.button_base = QPushButton("Button", self.central_area)
        self.button_base.setGeometry(375, 100, 50, 25)
        self.button_base.clicked.connect(self.def_button)

        self.value_percent_dosage = QLabel(self.central_area)
        self.value_percent_dosage.setStyleSheet("border: 1px ridge white")
        self.value_percent_dosage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value_percent_dosage.setGeometry(375, 35, 25, 25)

        self.slider = QSlider(Qt.Horizontal, self.central_area)
        self.slider.setGeometry(150, 50, 200, 25)
        self.slider.setMaximum(20)
        self.slider.valueChanged.connect(self.value_slider)

        self.setCentralWidget(self.central_area)
        self.statusBar().setStyleSheet("background: gray")

    @Slot(int)
    def value_slider(self):

        slider: QSlider = self.sender()
        self.value_percent_aroma = slider.value()
        self.value_percent_dosage.setText(str(slider.value()))

    @Slot()
    def def_button(self):
        if self.value_percent_aroma == 0:
            print("valeur incorrect")
        else:
            print(self.value_percent_aroma)
            print(type(self.value_percent_aroma))


app = QApplication(sys.argv)

window = Window()

window.show()
sys.exit(app.exec())
