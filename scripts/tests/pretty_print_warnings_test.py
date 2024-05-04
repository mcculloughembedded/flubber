import pytest
from pretty_printer import *

from ansi_colours import *

@pytest.fixture(autouse=True)
def setup_and_teardown(tmpdir):
    # Setup
    clearWarningsBuffer()

    yield # Run tests

    # Teardown

def test_single_warning(capsys):
    WARNING(displayText='Dummy Warning', filename='dummyFile', line=10)
    showWarningsBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"dummyFile:10 {colourise('warning', colour.BLUE)}: Dummy Warning\n"

def test_single_warning_file_not_specified():
    with pytest.raises(ValueError, match='File and line must be specified together.'):
        WARNING(displayText='Dummy Warning', line=10)

def test_single_warning_line_not_specified():
    with pytest.raises(ValueError, match='File and line must be specified together.'):
        WARNING(displayText='Dummy Warning', filename='dummyFile')

def test_single_warning_no_file(capsys):
    WARNING(displayText='Dummy Warning')
    showWarningsBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"{colourise('warning', colour.BLUE)}: Dummy Warning\n"

def test_print_buffer_is_used(capsys):
    WARNING(displayText='Dummy Warning')
    captured = capsys.readouterr()
    assert not captured.out

    WARNING(displayText='Dummy Warning', filename='dummyFile', line=10)
    captured = capsys.readouterr()
    assert not captured.out

def test_multiple_warnings(capsys):
    WARNING(displayText='Dummy Warning One')
    WARNING(displayText='Dummy Warning Two', filename='dummyFile', line=10)
    WARNING(displayText='Dummy Warning Three')
    showWarningsBuffer()

    captured = capsys.readouterr()
    assert captured.out == \
        f"{colourise('warning', colour.BLUE)}: Dummy Warning One\n" \
        f"dummyFile:10 {colourise('warning', colour.BLUE)}: Dummy Warning Two\n" \
        f"{colourise('warning', colour.BLUE)}: Dummy Warning Three\n"
