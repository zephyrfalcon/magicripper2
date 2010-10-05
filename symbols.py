# symbols.py
# Translate Gatherer image (symbol) descriptions to our own descriptions.

import re

symbols = {
    "black": "B",
    "red": "R",
    "blue": "U",
    "white": "W",
    "green": "G",
    "tap": "TAP",
    "variable colorless": "X",
    "red or white": "RW",
    "red or green": "RG",
    "black or green": "BG",
    "white or blue": "WU",
    "blue or red": "UR",
    "blue or black": "UB",
    "green or blue": "GU",
    "green or white": "GW",
    "white or black": "WB",
    "black or red": "BR",
    "two or blue": "2U",
    "two or black": "2B",
    "two or white": "2W",
    "two or green": "2G",
    "two or red": "2R",
    "untap": "UNTAP",
    "snow": "S",
}

re_number = re.compile("^\d+$")

def translate(symbol):
    if re_number.match(symbol):
        return symbol # numbers stay the same
    try:
        return symbols[symbol]
    except KeyError:
        raise KeyError("Unknown symbol: %r" % symbol)

rarities = {
    'rare': 'R',
    'uncommon': 'U',
    'common': 'C',
    'mythic rare': 'MR',
    'basic land': 'L',
    'special': 'S', # Time Spiral timeshifted cards
}

