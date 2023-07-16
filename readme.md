# Function Plotter

This is a Python GUI program that plots an arbitrary user-entered function using PySide6 and Matplotlib.

## Requirements

- Python 3.6 or above
- PySide6
- Matplotlib
- NumPy

## Features

- User can enter a mathematical function of `x` using the supported operators and functions.
- User can specify the minimum and maximum values of `x` for the plot range.
- The program supports functions such as `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, and the basic arithmetic operators.
- The plot is displayed in a simple and organized graphical user interface.
- Appropriate input validation is applied to ensure correct user input.
- Error messages are displayed to guide the user in case of invalid input.
- The validity of the entered function is checked to ensure it follows the allowed syntax and contains only supported functions and operators.
- The validity of the plot range is validated to ensure the minimum value is less than the maximum value.

## Usage

1. Install the required dependencies:

   ```shell
   pip install PySide6 matplotlib numpy
   ```

2. Run the program:

   ```shell
   python app.py
   ```

3. Enter a mathematical function in the "Enter function: y =" input field. For example:

   - Linear function: `2*x + 5`\
     ![Linear function](/example_screenshots/Linear_function.png)
   - Quadratic function: `x^2 + 3*x - 2`\
     ![Quadratic function](/example_screenshots/Quadratic_function.png)
   - Trigonometric function: `sin(x) + cos(2*x)`\
     ![Trigonometric function](/example_screenshots/Trigonometric_function.png)
   - Exponential function: `exp(x)`\
     ![Exponential function](/example_screenshots/Exponential_function.png)
   - Logarithmic function: `log(x)`\
     ![Logarithmic function](/example_screenshots/Logarithmic_function.png)
   - Rational function: `1 / (x^2 + 1)`\
     ![Rational function](/example_screenshots/Rational_function.png)
   - Square root function: `sqrt(x)`\
     ![Square root function](/example_screenshots/Square_root_function.png)

4. Specify the minimum and maximum values of `x` in the "Min x" and "Max x" input fields.

5. Click the "Plot" button to display the graph of the function within the specified range.

## Validate example

- Missed function
  ![Function missed](/example_screenshots/missed_function.png)
- Missed Range
  ![Range missed](/example_screenshots/Range_missed.png)!
- Function error for example: x+y \
  ![Function error](/example_screenshots/function_invalid_erroe.png)
- Min bigger than Max\
  ![min_vs_max_error](/example_screenshots/min_vs_max_error.png)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
