# app/operations/multiplication.py

from app.operations import Operation
from typing import Union

class Multiplication(Operation):
    """Performs multiplication of two numbers, inheriting from the base Operation class."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Calculate the product of two numbers after validating inputs.

        Args:
            a (Union[int, float]): The first number.
            b (Union[int, float]): The second number.

        Returns:
            float: The result of multiplying a by b.
        """
        # Validate inputs to ensure they are appropriate for multiplication
        self._validate_inputs(a, b)
        
        # Perform the multiplication
        result = a * b
        
        return result

