from pretty_printer import *

from ansi_colours import *

def test_print_info(capsys):
    INFO(displayText='Dummy Info')

    captured = capsys.readouterr()
    assert captured.out == f"{colourise('Dummy Info', colour.CYAN)}\n"
