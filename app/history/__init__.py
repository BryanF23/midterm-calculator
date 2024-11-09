import json
from typing import List
from app.calculation import Calculation

class History:
    """Manages the history of calculations with functionality to add, undo, clear, save, and load calculations."""

    def __init__(self):
        """Initialize an empty history list to store Calculation instances."""
        self._history: List[Calculation] = []

    def add_calculation(self, calculation: Calculation) -> None:
        """
        Add a Calculation object to the history.

        Args:
            calculation (Calculation): A Calculation object to record in the history.
        """
        self._history.append(calculation)

    def undo(self) -> str:
        """
        Remove and return the last calculation from history.

        Returns:
            str: Information about the undone calculation or a message if no history exists.
        """
        if not self._history:
            return "No history to undo."
        last_calculation = self._history.pop()
        return f"Undone: {last_calculation}"

    def clear(self) -> str:
        """
        Remove all calculations from history.

        Returns:
            str: Confirmation that history has been cleared.
        """
        self._history.clear()
        return "History cleared."

    def save(self, filename: str = "history.json") -> str:
        """
        Save the current history to a JSON file.

        Args:
            filename (str): The filename to save the history. Defaults to 'history.json'.

        Returns:
            str: Confirmation message that the history has been saved.
        """
        try:
            with open(filename, "w") as file:
                json.dump([calc.__dict__ for calc in self._history], file)
            return f"History saved to {filename}."
        except IOError:
            return f"Error: Could not save history to {filename}."

    def load(self, filename: str = "history.json") -> str:
        """
        Load calculation history from a JSON file.

        Args:
            filename (str): The filename to load history from. Defaults to 'history.json'.

        Returns:
            str: Confirmation that history has been loaded, or an error message if file issues occur.
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self._history = [Calculation(**entry) for entry in data]
            return f"History loaded from {filename}."
        except FileNotFoundError:
            return f"Error: {filename} not found."
        except json.JSONDecodeError:
            return f"Error: Failed to decode history data from {filename}."
        except TypeError:
            return "Error: Loaded data format is incorrect."

    def get_history(self) -> List[Calculation]:
        """
        Retrieve the complete calculation history.

        Returns:
            List[Calculation]: A list containing all Calculation instances in the history.
        """
        return self._history

