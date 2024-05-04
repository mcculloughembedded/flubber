from ansi_colours import *

def test_colourise_red():
    displayText = colourise('TEXT', colour.RED)
    assert displayText == '\033[31mTEXT\033[0m'

def test_colourise_blue():
    displayText = colourise('TEXT', colour.BLUE)
    assert displayText == '\033[1;34mTEXT\033[0m'

def test_colourise_green():
    displayText = colourise('TEXT', colour.GREEN)
    assert displayText == '\033[32mTEXT\033[0m'
