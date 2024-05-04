from enum import Enum

class colour(Enum):
    RED = 31
    GREEN = 32
    BLUE = '1;34'
    PURPLE = '1;35'
    CYAN = 36

def colourise(text: str, colour: colour):
    return f'\033[{colour.value}m{text}\033[0m'
