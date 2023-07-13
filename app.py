from PySide6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import re


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # build the main layout
        self.setWindowTitle("Function Plotter")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # define figure or chart GUI
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create widgets
        self.function_label = QLabel("Enter function: y = ")
        self.function_input = QLineEdit()
        self.minx_label = QLabel("Min x:")
        self.minx_input = QLineEdit()
        self.maxx_label = QLabel("Max x:")
        self.maxx_input = QLineEdit()
        self.submit_button = QPushButton("Plot")

        # Layout
        function_layout = QHBoxLayout()
        function_layout.addWidget(self.function_label)
        function_layout.addWidget(self.function_input)

        xrange_layout = QHBoxLayout()
        xrange_layout.addWidget(self.minx_label)
        xrange_layout.addWidget(self.minx_input)
        xrange_layout.addWidget(self.maxx_label)
        xrange_layout.addWidget(self.maxx_input)

        self.layout.addLayout(function_layout)
        self.layout.addLayout(xrange_layout)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.canvas)


if __name__ == "__main__":
    app = QApplication([])
    widget = PlotWidget()
    widget.show()
    app.exec()
