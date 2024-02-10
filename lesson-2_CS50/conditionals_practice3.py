'''
name = input('What is your name? ')

if name == 'Harry' or 'Hermoine' or 'Ron':
    print('Griffyndor')
elif name == 'Hermoine':
    print('Griffyndor')
else:
    print('Who?')
'''


##########  Using "MATCH" to replace lengthy elif and or statements ##########

import match

name = input('What is your name? ')

match name:
    case 'Harry' | 'Hermoine' | 'Ron':
        print('Gryffindor')
    case _:
        print('Who?')