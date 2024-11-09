from typing import Union
from app.operations import Operation

class Calculation:
    """Represents a calculation with an operation and two operands."""

    def __init__(self, operation: Operation, operand1: Union[int, float], operand2: Union[int, float]):
        """
        Initialize a Calculation instance with a specified operation and two operands.

        Args:
            operation (Operation): An instance of an Operation subclass (e.g., Addition, Subtraction).
            operand1 (Union[int, float]): The first operand in the calculation.
            operand2 (Union[int, float]): The second operand in the calculation.
        """
        self.operation = operation  # The operation to perform (e.g., Addition, Subtraction)
        self.operand1 = operand1    # First operand of the calculation
        self.operand2 = operand2    # Second operand of the calculation
        self.result: Union[int, float, None] = None  # Result is None until calculation is performed

    def execute(self) -> Union[int, float]:
        """
        Execute the calculation using the specified operation and operands, storing the result.

        Returns:
            Union[int, float]: The result of the calculation.
        """
        self.result = self.operation.calculate(self.operand1, self.operand2)  # Perform the operation
        return self.result

    def __repr__(self) -> str:
        """
        Return a string representation of the calculation, including operands, operation, and result.

        Returns:
            str: A formatted string showing operands, operation, and result (if calculated).
        """
        operation_name = self.operation.__class__.__name__.lower()  # Get operation name in lowercase
        result_display = self.result if self.result is not None else "Not calculated"
        return f"{self.operand1} {operation_name} {self.operand2} = {result_display}"


