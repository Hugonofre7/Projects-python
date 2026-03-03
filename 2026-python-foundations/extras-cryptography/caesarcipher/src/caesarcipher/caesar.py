"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This program hacks messages encrypted with the Caesar cipher by doing 
a brute force attack against every possible key.
More info at https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, cryptography math"""

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

#let the user enter the message to hack:
print('Enter the encrypted Caesar cipher message to hack:')
message = input('> ')

#Every possible symbol that can be encrypted/decrypted:
#(This must match the SYMBOLS used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(SYMBOLS)): # Loop through every possible key.
    translated = ''

    for key in range(len(SYMBOLS)): # Loop through every possible key.
        translated = ''

        #Decrypt each symbol in the message:
        for symbol in message:
            