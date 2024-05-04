import pytest
from pretty_printer import *

from ansi_colours import *

@pytest.fixture(autouse=True)
def setup_and_teardown(tmpdir):
    # Setup
    clearRemarksBuffer()

    yield # Run tests

    # Teardown

def test_single_remark(capsys):
    REMARK(displayText='Dummy Remark', filename='dummyFile', line=10)
    showRemarksBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"dummyFile:10 {colourise('remark', colour.PURPLE)}: Dummy Remark\n"

def test_single_remark_file_not_specified():
    with pytest.raises(ValueError, match='File and line must be specified together.'):
        REMARK(displayText='Dummy Remark', line=10)

def test_single_remark_line_not_specified():
    with pytest.raises(ValueError, match='File and line must be specified together.'):
        REMARK(displayText='Dummy Remark', filename='dummyFile')

def test_single_remark_no_file(capsys):
    REMARK(displayText='Dummy Remark')
    showRemarksBuffer()

    captured = capsys.readouterr()
    assert captured.out == f"{colourise('remark', colour.PURPLE)}: Dummy Remark\n"

def test_print_buffer_is_used(capsys):
    REMARK(displayText='Dummy Remark')
    captured = capsys.readouterr()
    assert not captured.out

    REMARK(displayText='Dummy Remark', filename='dummyFile', line=10)
    captured = capsys.readouterr()
    assert not captured.out

def test_multiple_remarks(capsys):
    REMARK(displayText='Dummy Remark One')
    REMARK(displayText='Dummy Remark Two', filename='dummyFile', line=10)
    REMARK(displayText='Dummy Remark Three')
    showRemarksBuffer()

    captured = capsys.readouterr()
    assert captured.out == \
        f"{colourise('remark', colour.PURPLE)}: Dummy Remark One\n" \
        f"dummyFile:10 {colourise('remark', colour.PURPLE)}: Dummy Remark Two\n" \
        f"{colourise('remark', colour.PURPLE)}: Dummy Remark Three\n"
