import pytest
from app import (
    validate_expression, substitute_constants, func_2_string, validate_inputs, MainWindow
)


def test_validate_expression_valid():
    # Valid expressions should not raise an exception
    valid_expressions = [
        "x",
        "sin(x) + 2",
        "3*x^2 + 2*x + 1",
        "log(x) / sqrt(x)",
        "exp(-x)",
        "tan(x)"
    ]
    for expression in valid_expressions:
        validate_expression(expression)  # No exception should be raised


def test_validate_expression_invalid():
    # Invalid expressions should raise a ValueError
    invalid_expressions = [
        "x^2 + 2y",    # 'y' is not allowed
        "sin2(x)",     # 'sin2' is not allowed
        "log(x) +",    # Incomplete expression
        "sqrt(1/x)"    # Division by zero
    ]
    for expression in invalid_expressions:
        with pytest.raises(ValueError):
            validate_expression(expression)


def test_substitute_constants():
    expression = "sin(pi*x) + sqrt(2) * log(exp(1))"
    expected_result = "np.sin(np.pi*x) + np.sqrt(2) * np.log(np.exp(1))"
    result = substitute_constants(expression)
    assert result == expected_result


def test_func_2_string():
    expression = "x^2 + 2*x + 1"
    func = func_2_string(expression)
    x = [0, 1, 2, 3]
    expected_result = [1, 4, 9, 16]
    result = func(x)
    assert result == expected_result


def test_validate_inputs_valid():
    # Valid inputs should not raise an exception
    function = "2*x + 5"
    min_x = "-10"
    max_x = "10"
    validate_inputs(function, min_x, max_x)  # No exception should be raised


def test_validate_inputs_invalid():
    # Invalid inputs should raise a ValueError
    invalid_inputs = [
        ("", "-10", "10"),  # Empty function
        ("2*x + 5", "", "10"),  # Empty min_x
        ("2*x + 5", "10", ""),  # Empty max_x
        ("2*x + 5", "10a", "20"),  # Non-numeric min_x
        ("2*x + 5", "10", "20a"),  # Non-numeric max_x
        ("2*x + 5", "20", "10"),  # min_x > max_x
    ]
    for function, min_x, max_x in invalid_inputs:
        with pytest.raises(ValueError):
            validate_inputs(function, min_x, max_x)

def test_plot_btn_submitted_valid():
    # Valid inputs should not raise an exception
    widget = MainWindow()
    widget.function_input.setText("2*x + 5")
    widget.min_x_input.setText("-10")
    widget.max_x_input.setText("10")

    # Call the plot_btn_submitted method
    widget.plot_btn_submitted()

    # No exception should be raised


def test_plot_btn_submitted_invalid():
    # Invalid inputs should raise a ValueError
    widget = MainWindow()
    widget.function_input.setText("")  # Empty function
    widget.min_x_input.setText("-10")
    widget.max_x_input.setText("10")

    with pytest.raises(ValueError):
        widget.plot_btn_submitted()

    widget.function_input.setText("2*x + 5")
    widget.min_x_input.setText("")  # Empty min_x
    widget.max_x_input.setText("10")

    with pytest.raises(ValueError):
        widget.plot_btn_submitted()

    widget.function_input.setText("2*x + 5")
    widget.min_x_input.setText("-10")
    widget.max_x_input.setText("")  # Empty max_x

    with pytest.raises(ValueError):
        widget.plot_btn_submitted()

    widget.function_input.setText("2*x + 5")
    widget.min_x_input.setText("10a")  # Non-numeric min_x
    widget.max_x_input.setText("20")

    with pytest.raises(ValueError):
        widget.plot_btn_submitted()

    widget.function_input.setText("2*x + 5")
    widget.min_x_input.setText("10")
    widget.max_x_input.setText("20a")  # Non-numeric max_x

    with pytest.raises(ValueError):
        widget.plot_btn_submitted()

    widget.function_input.setText("2*x + 5")
    widget.min_x_input.setText("20")  # min_x > max_x
    widget.max_x_input.setText("10")

    with pytest.raises(ValueError):
        widget.plot_btn_submitted()


if __name__ == "__main__":
    pytest.main(["-v"])
