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

# Select percent aroma --------------------------------------------------------

        self.label_percent_dosage = QLabel(self.central_area)
        self.label_percent_dosage.setText("Percent Dosage Aroma")
        self.label_percent_dosage.setGeometry(175, 25, 175, 25)

        self.slider = QSlider(Qt.Horizontal, self.central_area)
        self.slider.setGeometry(150, 50, 200, 25)
        self.slider.setMaximum(20)
        self.slider.valueChanged.connect(self.value_slider)

        self.setCentralWidget(self.central_area)
        self.statusBar().setStyleSheet("background: gray")

# Select quantity total -------------------------------------------------------

        self.label_quantity_total = QLabel(self.central_area)
        self.label_quantity_total.setText("Quantity Total")
        self.label_quantity_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_quantity_total.setStyleSheet("border: 1px ridge white")
        self.label_quantity_total.setGeometry(175, 100, 175, 25)

        self.entry_quantity_total = QLineEdit(self.central_area)
        self.entry_quantity_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_quantity_total.setStyleSheet("border: 1px ridge white")
        self.entry_quantity_total.setGeometry(375, 100, 75, 25)
        self.entry_quantity_total.textChanged.connect(
            self.value_entry_quantity_total)

        self.quantity_total = QLabel(self.central_area)
        self.quantity_total.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.quantity_total.setStyleSheet("border: 1px ridge white")
        self.quantity_total.setGeometry(200, 135, 125, 25)

        self.button = QPushButton("Valid", self.central_area)
        self.button.setGeometry(375, 135, 75, 25)
        self.button.clicked.connect(self.def_button)

# Select aroma ----------------------------------------------------------------

        self.label_aroma = QLabel(self.central_area)
        self.label_aroma.setText("Aroma")
        self.label_aroma.setStyleSheet("border: 1px ridge white")
        self.label_aroma.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_aroma.setGeometry(175, 200, 175, 25)

        self.entry_aroma = QLineEdit(self.central_area)
        self.entry_aroma.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_aroma.setStyleSheet("border: 1px ridge white")
        self.entry_aroma.setGeometry(375, 200, 75, 25)

        self.aroma = QLabel(self.central_area)
        self.aroma.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.aroma.setStyleSheet("border: 1px ridge white")
        self.aroma.setGeometry(200, 235, 125, 25)

        self.button_aroma = QPushButton("Valid", self.central_area)
        self.button_aroma.setGeometry(375, 235, 75, 25)
        self.button_aroma.clicked.connect(self.def_button)

# Select base -----------------------------------------------------------------

        self.base_widget = QWidget()
        
        self.label_base = QLabel(self.central_area)
        self.label_base.setText("Base")
        self.label_base.setStyleSheet("border: 1px ridge white")
        self.label_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_base.setGeometry(175, 300, 175, 25)

        self.entry_base = QLineEdit(self.central_area)
        self.entry_base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry_base.setStyleSheet("border: 1px ridge white")
        self.entry_base.setGeometry(375, 300, 75, 25)

        self.base = QLabel(self.central_area)
        self.base.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.base.setStyleSheet("border: 1px ridge white")
        self.base.setGeometry(200, 335, 125, 25)

        self.button_base = QPushButton("Valid", self.central_area)
        self.button_base.setGeometry(375, 335, 75, 25)
        self.button_base.clicked.connect(self.def_button)

        self.value_percent_dosage = QLabel(self.central_area)
        self.value_percent_dosage.setStyleSheet("border: 1px ridge white")
        self.value_percent_dosage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value_percent_dosage.setGeometry(375, 35, 25, 25)
        



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

    @Slot()
    def value_entry_quantity_total(self):
        print(self.entry_quantity_total.text)


app = QApplication(sys.argv)

window = Window()

window.show()
sys.exit(app.exec())
