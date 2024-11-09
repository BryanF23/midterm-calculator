"""
Tests for the History class and its functionality in the calculator app.

Covers adding, undoing, clearing, saving, and loading calculation history.
"""
from unittest.mock import mock_open, patch
import pytest
from app.history import History
from app.calculation import Calculation # type: ignore
from app.operations.addition import Addition # type: ignore
from app.operations.subtraction import Subtraction # type: ignore

# Fixtures
@pytest.fixture
def history():
    """Fixture to provide a fresh History instance for each test."""
    return History()

@pytest.fixture
def sample_calculation():
    """Fixture to create a sample Calculation for testing purposes."""
    operation = Addition()
    return Calculation(operation=operation, operand1=5, operand2=3)

# Positive Tests
@pytest.mark.parametrize("calculation", [
    Calculation(operation=Addition(), operand1=2, operand2=3),
    Calculation(operation=Subtraction(), operand1=10, operand2=5),
])
def test_add_calculation(history, calculation):
    """Test adding a calculation to history."""
    history.add_calculation(calculation)
    assert history.get_history()[-1] == calculation  # Verify calculation was added

def test_undo_with_history(history, sample_calculation):
    """Test undo functionality when history contains calculations."""
    history.add_calculation(sample_calculation)
    result = history.undo()
    assert result == f"Undone: {sample_calculation}"
    assert not history.get_history()  # Ensure history is empty after undo

def test_clear_history(history, sample_calculation):
    """Test clearing all calculations from history."""
    history.add_calculation(sample_calculation)
    result = history.clear()
    assert result == "History cleared."
    assert not history.get_history()  # History should be empty

def test_save_load_history_without_serialization(history, sample_calculation):
    """Test saving and loading history from a file with mocked I/O."""
    history.add_calculation(sample_calculation)

    with patch("builtins.open", mock_open()) as mocked_file, patch("json.dump") as mocked_json_dump:
        save_result = history.save("test_history.json")
        mocked_file.assert_called_once_with("test_history.json", 'w')
        mocked_json_dump.assert_called_once_with(
            [calc.__dict__ for calc in history.get_history()], mocked_file())
        assert save_result == "History saved to test_history.json."

    mock_data = '[{"operand1": 5, "operand2": 3, "operation": "Addition"}]'

    with patch("builtins.open", mock_open(read_data=mock_data)) as mocked_file, \
         patch("json.load", return_value=[{'operand1': 5, 'operand2': 3, 'operation': 'Addition'}]):
        load_result = history.load("test_history.json")
        mocked_file.assert_called_once_with("test_history.json", 'r')
        assert load_result == "History loaded from test_history.json."
        assert len(history.get_history()) == 1
        assert history.get_history()[0].operand1 == 5

# Negative Tests
def test_undo_with_empty_history(history):
    """Test undoing when history is empty."""
    result = history.undo()
    assert result == "No history to undo."

@pytest.mark.parametrize("filename", ["non_existent.json", "invalid.json"])
def test_load_file_not_found(history, filename):
    """Test loading history from a non-existent file."""
    result = history.load(filename)
    assert result == f"Error: {filename} not found."

def test_load_invalid_json_format(history, tmpdir):
    """Test loading history from a file with corrupted JSON data."""
    filename = tmpdir.join("invalid_history.json")

    with open(str(filename), "w", encoding="utf-8") as file:
        file.write("{invalid json}")

    result = history.load(str(filename))
    assert "Error: Failed to decode history data" in result

