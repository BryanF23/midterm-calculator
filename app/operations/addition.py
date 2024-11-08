# app/operations/addition.py

from app.operations import Operation
from typing import Union

class Addition(Operation):
    """Performs the addition of two numbers, inheriting from the base Operation class."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Calculate the sum of two numbers after validating them.

        Args:
            a (Union[int, float]): The first number.
            b (Union[int, float]): The second number.

        Returns:
            float: The result of adding a and b.
        """
        # Validate inputs to ensure they're appropriate for addition
        self._validate_inputs(a, b)
        
        # Perform the addition operation
        result = a + b
        
        return result
