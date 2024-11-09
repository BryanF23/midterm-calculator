from abc import ABC, abstractmethod
from typing import Union

class Operation(ABC):
    """Abstract base class representing a generic operation for a calculator."""

    def _validate_inputs(self, operand1: Union[int, float], operand2: Union[int, float]) -> None:
        """
        Validate that both inputs are of type int or float.

        Args:
            operand1 (Union[int, float]): The first operand.
            operand2 (Union[int, float]): The second operand.

        Raises:
            TypeError: If either operand1 or operand2 is not a number (int or float).
        """
        if not all(isinstance(arg, (int, float)) for arg in (operand1, operand2)):
            raise TypeError(
                f"Invalid input types: operand1 is {type(operand1).__name__}, operand2 is {type(operand2).__name__}. "
                "Expected int or float."
            )

    @abstractmethod
    def calculate(self, operand1: Union[int, float], operand2: Union[int, float]) -> float:
        """
        Perform the calculation between two operands.
        This method must be implemented by subclasses.

        Args:
            operand1 (Union[int, float]): The first operand.
            operand2 (Union[int, float]): The second operand.

        Returns:
            float: The result of the calculation.
        """
        pass  # This is an abstract method, to be defined in subclasses

