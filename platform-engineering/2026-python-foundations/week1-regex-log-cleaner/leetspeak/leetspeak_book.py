"""Leetspeak, by Al Sweigart al@inventwithpython.com
Translate English messages into 133t5p34]<.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, word"""

import random

try:
    import pyperclip # pyperclip copies text to the clipboard.
except ImportError:
    pass # If pyperclip is not installed, do nothing. It's no big deal.

def main():
    print('''L33t5p34]<, (leetspeak)
By Al Sweigart al@inventwithpython.com

Enter your leet message:''')
    english = input('> ')
    print()
    leetspaeak = englishToLeetspeak(english)
    print(leetspaeak)
    
    try:
        # Try to use pyperclip will raise a NameError exception if
        # it wasn't imported:
        pyperclip.copy(leetspaeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass # Do nothing if pyperclip wasn't installed.
    
def englishToLeetspeak(message):
    """Convert the English string in message to leetspeak."""
    # Make sure all the keys in 'charMapping' are lowercase.
    charMapping = {
    'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
    'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],     'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
    'v': ['\\/']}
    leetspeak = ''
    for char in message: #Check each character:
        #There is a 70% chance that the character will be translated to leetspeak.
        if char.lower() in charMapping and random.random() <= 0.7:
            possibleLeetReplacements = charMapping[char.lower()]
            leetReplacement = random.choice(possibleLeetReplacements)
            leetspeak = leetspeak + leetReplacement
        else:
            # Don't translate this character:
            leetspeak = leetspeak + char
    return leetspeak
# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    main()