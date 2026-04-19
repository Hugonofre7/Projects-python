"""sPoNgECasE, by Al Sweigart al@inventwithpython.com
Translates Eglish message into sPOnGEtExT.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, word"""

import random

try:
    import pyperclip  #pyperclip copies text to the clipboard.
except ImportError:
    pass  #If pyperclip is not installed, do nothing. It's no big deal.

def main():
    """Run the Spongetext program."""
    print('''sPoNgECasE, by Al Sweigart AL@iNvEnTwIthpYtHOn.COM
    
eNtEr YouUr MeSsAgE:''')
    spongetext =  englishToSpongetext(input('> '))
    print()
    print(spongetext)
    
    try:
        pyperclip.copy(spongetext)
        print('(cOpIEd SpOnGeTeXT tO cLiPBoArD.)')
    except:
        pass  #Do nothing if pyperclip is not installed.
    
def englishToSpongetext(message):
    """Return the spongetext from of the given string."""
    spongetext = ''
    useUpper = False
    
    for character in message:
        if not character.isalpha():
            spongetext += character
            continue
        
        if useUpper:
           spongetext += character.upper()
        else:
           spongetext += character.lower()
    
        #Flip the case, 90% of the time.
        if random.randint(1, 100) <= 90:
           useUpper = not useUpper  #Flip the case.
    return spongetext

# If this program was run (instead of imported as a module), run the game:
if __name__ == '__main__':
    main()
    