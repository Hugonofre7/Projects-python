"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This program hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
More info at https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography math"""

try:
    import pyperclip # pyperclip copies text to the clipboard.
except ImportError:
    
    pass # If pyperclip is not installed, do nothing. It's no big deal.
# Every possible symbol that can be encrypted/decrypted:
# (!) You can add  numbers and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example,  a key of 2 means the letter A is')
print('encrypted to C, the letter B is encrypted into D, and so on.')
print()

# Let the user enter if they are encrypting or decrypting:
while True: #Keep asking until the user enters e or d.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("Please enter the letter e or d.")
    
# Let the user enter the key to use:
while True: #Keep asking until the user enters a valid key.
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue # If the response is not a number, ask again.
    
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break # If the response is a valid key, exit the loop.
    
# Let the user enter the message to encrypt/decrypt:
print('Enter the message to {}.'.format(mode))
message = input('> ')

# Caesar cipher only works on letters.
message = message.upper()

# Store the encrypted/decrypted form of the message:
translated = ''

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
            
            #Handle the wrap-around if num is larger than the length of
            #SYMBOLS or if num is less than 0.
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
            
            # Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol
        
# Display the encrypted/decrypted string to the scream:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass # Do nothing if pyperclip wasn't installed.
