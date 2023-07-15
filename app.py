from PySide6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import re
import math


# list of allowed words to be entered by the user
ALLOWED_WORDS = ["sin", "cos", "tan", "exp", "+", "-", "*", "/", "x"]

# message format
message = f"I'm sorry, any variable else 'x' is not allowed in your math expression. \n\n"
message += f"Please enter a function of 'x' only. For example: \n"
message += "  - 5*x^3 + 2/x - 1\n"
message += "\nYou can use these math symbols:\n"
message += f" - Functions: {', '.join(ALLOWED_WORDS[:-4])}\n"
message += f" - Operators: {', '.join(ALLOWED_WORDS[-4:])}\n\n"
message += "Please update your expression to use only the allowed variable and functions."

replacements = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**', }


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
        # define error dialog
        self.error_dialog = QMessageBox()

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

        self.submit_button.clicked.connect(lambda _: self.plot_btn_submitted())

    def plot_btn_submitted(self):
        try:
            print(self.function_input.text())
            y = func_2_string(self.function_input.text())
        except ValueError as e:
            self.error_dialog.setWindowTitle("Error!")
            self.error_dialog.setText(str(e))
            self.error_dialog.show()
        return


def validate_expression(expression):
    """Check that expression contains only allowed words and symbols"""
    for word in re.findall(r"[a-zA-Z_]+", expression):
        if word not in ALLOWED_WORDS:
            raise ValueError(message)


def substitute_constants(expression):
    """Replace predefined constant values"""
    constants = {"pi": str(math.pi),
                 'sin': 'np.sin',
                 'cos': 'np.cos',
                 'exp': 'np.exp',
                 'sqrt': 'np.sqrt',
                 '^': '**'}
    for old, new in constants.items():
        expression = expression.replace(old, new)
    return expression


def func_2_string(expression):
    """Convert a string math expression to a function"""

    # Validate input
    validate_expression(expression)

    # Substitute known constants
    expression = substitute_constants(expression)

    # Append x*0 to handle constant expressions
    if "x" not in expression:
        expression += "+0*x"
    print(expression)

    def func():
        return eval(expression)

    return func


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
