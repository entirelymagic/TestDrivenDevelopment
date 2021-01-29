import pytest

from pytest import raises
from LineReader import readFromFile
from unittest.mock import MagicMock

# TODO: can Call readFromFile
# TODO: readFromFile returns correct string
# TODO: readFromFile throws exception when file doesn't exist


@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


def test_returnsCorrectString(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = readFromFile('baubau')
    mock_open.assert_called_once_with('baubau', 'r')
    assert result == "test line"


def test_trowsExceptionWithBadFile(monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = readFromFile('baubau')
