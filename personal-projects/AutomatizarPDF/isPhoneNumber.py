def is_phone_number(text):
    if len(text) != 12: #El telefono debe de tener 12 caracteres
        return False
    for i in range(0, 3): #Los primeros 3 caracteres deben de ser digitos
        if not text[i].isdecimal():
            return False
    if text[3] != '-': #El cuarto caracter debe de ser un guion
        return False
    for i in range(4, 7): #Los siguientes tres caracteres deben de ser digitos
        if not text[i].isdecimal():
            return False
    if text[7] != '-': #El octavo caracter debe de ser un guion
        return False
    for i in range(8, 12): #Los ultimos cuatro caracteres deben de ser digitos
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))
print(is_phone_number('415-555-4242'))
print('Is Moshi moshi a phone number?', is_phone_number('Moshi moshi'))
print(is_phone_number('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
  segment = message[i:i+12]
  if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')


import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
match_obj.group()
'415-555-4242'

"""
import re
phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.')
mo.group(1)  # Returns the first group of the matched text
'415'
mo.group(2)  # Returns the second group of the matched text
'555-4242'
mo.group(0)  # Returns the full matched text
'415-555-4242'
mo.group()  # Also returns the full matched text
'415-555-4242'

>>> import re
>>> pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  # This regex has no groups.
>>> pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']
>>> import re
>>> pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # This regex has groups.
>>> pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]

"""
