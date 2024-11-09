# app/operations/division.py

from app.operations import Operation
from typing import Union

class Division(Operation):
    """Performs division of two numbers, inheriting from the base Operation class."""

    def calculate(self, a: Union[int, float], b: Union[int, float]) -> float:
        """
        Calculate the division of two numbers after validating inputs.

        Args:
            a (Union[int, float]): The numerator.
            b (Union[int, float]): The denominator.

        Returns:
            float: The result of dividing a by b.

        Raises:
            ValueError: If the denominator (b) is zero.
        """
        # Validate inputs to ensure they are appropriate for division
        self._validate_inputs(a, b)
        
        # Check for division by zero and raise an error if needed
        if b == 0:
            raise ValueError("Division by zero is undefined.")
        
        # Perform the division
        result = a / b
        
        return result

