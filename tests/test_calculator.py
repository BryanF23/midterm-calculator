"""Unit tests for the Calculator class."""
# pylint: disable=redefined-outer-name
from typing import Literal
import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance for testing."""
    return Calculator()

@pytest.mark.parametrize("command, args, expected_output", [
    ("add", (1, 2), 3),
    ("subtract", (5, 3), 2),
    ("multiply", (2, 4), 8),
    ("divide", (8, 2), 4),
    ("divide", (1, 0), "Error: Division by zero is undefined."),  # Updated message
    ("unknown", (1, 2), "Error: Unknown command.")
])
def test_execute_command(calculator: Calculator, command: str, args: tuple[int, int], expected_output: str):
    """Test the execute_command method for various commands."""
    result = calculator.execute_command(command, *args)
    
    # Check if the output matches the expected result or error message
    assert result == expected_output


def test_show_help(calculator: Calculator):
    """Test the show_help method to ensure it returns the correct help text."""
    expected_help_text = (
        "Available commands:\n"
        "\n"
        "Operation Commands:\n"
        "- add: Add two numbers\n"
        "- subtract: Subtract the second number from the first\n"
        "- multiply: Multiply two numbers\n"
        "- divide: Divide the first number by the second\n"
        "\n"
        "History Commands:\n"
        "- undo: Undo the last calculation\n"
        "- clear: Clear the calculation history\n"
        "- history: Read the calculation history\n"
        "\n"
        "File Commands:\n"
        "- save: Save the current history to a file\n"
        "- load: Load history from a file\n"
        "\n"
        "General Commands:\n"
        "- help: Display this help message\n"
        "- exit/quit: Exit the calculator"
    )
    assert calculator.show_help() == expected_help_text

def test_exit_calculator(calculator: Calculator):
    """Test the exit_calculator method to ensure it returns the correct exit message."""
    assert calculator.exit_calculator() == "Exiting the calculator. Goodbye!"

def test_exit_command(calculator: Calculator):
    """Test the exit command to ensure it calls the exit_calculator method."""
    result = calculator.execute_command('exit')
    assert result == "Exiting the calculator. Goodbye!"

def test_invalid_argument_count(calculator: Calculator):
    """Test handling of invalid argument count."""
    result = calculator.execute_command('add', 1)  # Only one argument
    assert result == "Error: Invalid number of arguments. Please provide two numbers."

    result = calculator.execute_command('add')  # No arguments
    assert result == "Error: Invalid number of arguments. Please provide two numbers."

def test_read_history(calculator: Calculator):
    """Test read_history to ensure it retrieves and displays history correctly."""

    # Perform some operations
    calculator.execute_command('add', 5, 3)         # 5 + 3 = 8
    calculator.execute_command('subtract', 10, 4)    # 10 - 4 = 6
    calculator.execute_command('multiply', 2, 3)     # 2 * 3 = 6

    # Retrieve the history using the 'history' command
    history_output = calculator.execute_command('history')
    # Check that each calculation string is in the history output
    assert "5 addition 3 = 8" in str(history_output[0])
    assert "10 subtraction 4 = 6" in str(history_output[1])
    assert "2 multiplication 3 = 6" in str(history_output[2])
    
    class Calculator:
        def execute_command(self, command, *args):
            if command == "add":
                return sum(args)
            elif command == "subtract":
                return args[0] - args[1]
            elif command == "multiply":
                return args[0] * args[1]
            elif command == "divide":
                if args[1] == 0:
                    return "Error: Cannot divide by zero"  # Fix the error message here
                return args[0] / args[1]
            else:
                return "Error: Unknown command."
