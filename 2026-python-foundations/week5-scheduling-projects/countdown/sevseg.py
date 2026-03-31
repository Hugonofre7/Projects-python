"""Sevseg, by Al Sweigart al@inventwithpython.com
A seven-segment number display module.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, module"""


def getSevSegStr(number, minWidth=0):
    """Return a string for displaying a number on a seven-segment display."""
    number = str(number).zfill(minWidth)
    
    # Define the segments for each digit 0-9
    segments = {
        '0': [' _ ', '| |', '|_|'],
        '1': ['   ', '  |', '  |'],
        '2': [' _ ', ' _|', '|_ '],
        '3': [' _ ', ' _|', ' _|'],
        '4': ['   ', '|_|', '  |'],
        '5': [' _ ', '|_ ', ' _|'],
        '6': [' _ ', '|_ ', '|_|'],
        '7': [' _ ', '  |', '  |'],
        '8': [' _ ', '|_|', '|_|'],
        '9': [' _ ', '|_|', ' _|'],
        ' ': ['   ', '   ', '   ']
    }
    
    # Build the three lines of the display
    lines = ['', '', '']
    for i, digit in enumerate(number):
        seg = segments.get(digit, segments[' '])
        for j in range(3):
            lines[j] += seg[j]
        if i != len(number) - 1:
            for j in range(3):
                lines[j] += ' '
    
    return '\n'.join(lines)