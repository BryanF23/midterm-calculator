# app/operations/subtraction.py

from app.operations import Operation
from typing import Union

class Subtraction(Operation):
    """Performs the subtraction of one number from another."""

    def calculate(self, minuend: Union[int, float], subtrahend: Union[int, float]) -> float:
        """
        Calculate the difference between two numbers.

        Args:
            minuend (Union[int, float]): The number to subtract from.
            subtrahend (Union[int, float]): The number to be subtracted.

        Returns:
            float: The result of minuend minus subtrahend.
        """
        self._validate_inputs(minuend, subtrahend)  # Validate the inputs are numbers
        return minuend - subtrahend

