import sys
import re
import math
import numpy as np
from PySide6.QtWidgets import (
    QApplication, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# list of allowed words to be entered by the user
ALLOWED_FUNCTIONS = ["sin", "cos", "tan", "exp",
                     "log", "sqrt", "+", "-", "*", "/", "^", "x"]

# message format
message = f"I'm sorry, any variable else 'x' is not allowed in your math expression. \n\n"
message += f"Please enter a function of 'x' only. For example: \n"
message += "  - 5*x^3 + 2/x - 1\n"
message += "\nYou can use these math symbols:\n"
message += f" - Functions: {', '.join(ALLOWED_FUNCTIONS[:-4])}\n"
message += f" - Operators: {', '.join(ALLOWED_FUNCTIONS[-4:])}\n\n"
message += "Please update your expression to use only the allowed variable and functions."


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
        self.axes = self.figure.subplots()

        # Create widgets
        self.function_label = QLabel("Enter function: y = ")
        self.function_input = QLineEdit()
        self.min_x_label = QLabel("Min x:")
        self.min_x_input = QLineEdit()
        self.max_x_label = QLabel("Max x:")
        self.max_x_input = QLineEdit()
        self.submit_button = QPushButton("Plot")
        # define error dialog
        self.error_dialog = QMessageBox()

        # Layout
        function_layout = QHBoxLayout()
        function_layout.addWidget(self.function_label)
        function_layout.addWidget(self.function_input)

        xrange_layout = QHBoxLayout()
        xrange_layout.addWidget(self.min_x_label)
        xrange_layout.addWidget(self.min_x_input)
        xrange_layout.addWidget(self.max_x_label)
        xrange_layout.addWidget(self.max_x_input)

        self.layout.addLayout(function_layout)
        self.layout.addLayout(xrange_layout)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.canvas)

        self.submit_button.clicked.connect(self.plot_btn_submitted)
        self.function_input.textChanged.connect(self.handle_function_changed)
        self.min_x_input.textChanged.connect(self.handle_function_changed)
        self.max_x_input.textChanged.connect(self.handle_function_changed)

    def plot_btn_submitted(self):
        try:
            fn = self.function_input.text()
            mn = self.min_x_input.text()
            mx = self.max_x_input.text()
            validate_inputs(fn, mn, mx)
            self.plot_function(fn, mn, mx)

        except ValueError as e:
            self.error_dialog.setWindowTitle("Error!")
            self.error_dialog.setText(str(e))
            self.error_dialog.show()
        return

    def handle_function_changed(self, text):
        """Handle function text changed"""
        try:
            fn = self.function_input.text()
            mn = self.min_x_input.text()
            mx = self.max_x_input.text()
            validate_inputs(fn, mn, mx)
            self.plot_function(fn, mn, mx)
        except:
            pass

    def plot_function(self, fn_text, fn_min, fn_max):
        """Plot the function"""
        fn_max = float(fn_max)
        fn_min = float(fn_min)
        x = np.linspace(fn_min, fn_max, 1000)
        y = func_2_string(fn_text)(x)
        self.axes.clear()
        self.axes.plot(x, y)
        self.canvas.draw()


def validate_expression(expression):
    """Check that expression contains only allowed words and symbols"""
    for word in re.findall(r"[a-zA-Z_]+", expression):
        if word not in ALLOWED_FUNCTIONS:
            raise ValueError(message)


def substitute_constants(expression):
    """Replace predefined constant values"""
    constants = {
        "pi": str(math.pi),
        "sin": "np.sin",
        "cos": "np.cos",
        'tan': 'np.tan',
        "exp": "np.exp",
        "sqrt": "np.sqrt",
        'log': 'np.log',
        "^": "**",
    }
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

    def func(x):
        return eval(expression)

    return np.vectorize(func)


def validate_inputs(function, min_x, max_x):
    # Validate function
    if not function.strip():
        raise ValueError("Please enter a function to plot")

    # Validate range inputs
    if not min_x or not max_x:
        raise ValueError("Range values cannot be empty")

    if not re.fullmatch(r"[-+]?\d*\.?\d+", min_x) or not re.fullmatch(r"[-+]?\d*\.?\d+", max_x):
        raise ValueError("Range inputs must be numeric")

    min_x = float(min_x)
    max_x = float(max_x)

    if min_x > max_x:
        raise ValueError("Minimum value must be less than maximum")

    # Function validation
    try:
        func_2_string(function)
    except Exception as e:
        raise ValueError(message) from e


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
