import pytest
from pretty_printer import *

from ansi_colours import *

@pytest.fixture(autouse=True)
def setup_and_teardown(tmpdir):
    # Setup
    clearErrorsBuffer()

    yield # Run tests

    # Teardown

def test_single_error(capsys):
    ERROR(displayText='Dummy Error', filename='dummyFile', line=10)
    showErrorsBuffer()

    captured = capsys.readouterr()
    assert captured.out == \
        f"dummyFile:10 {colourise('error: Dummy Error', colour.RED)}\n"

def test_single_error_file_not_specified():
    with pytest.raises(ValueError, match='File and line must be specified together.'):
        ERROR(displayText='Dummy Error', line=10)

def test_single_error_line_not_specified():
    with pytest.raises(ValueError, match='File and line must be specified together.'):
        ERROR(displayText='Dummy Error', filename='dummyFile')

def test_single_error_no_file(capsys):
    ERROR(displayText='Dummy Error')
    showErrorsBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"{colourise('error: Dummy Error', colour.RED)}\n"

def test_print_buffer_is_used(capsys):
    ERROR(displayText='Dummy Error')
    captured = capsys.readouterr()
    assert not captured.out

    ERROR(displayText='Dummy Error', filename='dummyFile', line=10)
    captured = capsys.readouterr()
    assert not captured.out

def test_multiple_errors(capsys):
    ERROR(displayText='Dummy Error One')
    ERROR(displayText='Dummy Error Two', filename='dummyFile', line=10)
    ERROR(displayText='Dummy Error Three')
    showErrorsBuffer()

    captured = capsys.readouterr()
    assert captured.out == \
        f"{colourise('error: Dummy Error One', colour.RED)}\n" \
        f"dummyFile:10 {colourise('error: Dummy Error Two', colour.RED)}\n" \
        f"{colourise('error: Dummy Error Three', colour.RED)}\n"
