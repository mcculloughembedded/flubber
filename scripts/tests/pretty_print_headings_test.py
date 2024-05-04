from pretty_printer import *

from ansi_colours import *

def test_print_headings(capsys):
    HEADING(displayText='Dummy Heading')

    captured = capsys.readouterr()
    assert captured.out == f"{colourise('Dummy Heading', colour.GREEN)}\n"
