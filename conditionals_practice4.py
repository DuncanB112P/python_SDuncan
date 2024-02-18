
'''
name = input('What\'s your name? ')

if name == 'Harry' or name == 'Ron' or name == 'Hermione':
    print('Griffyndor')
elif name == 'Draco':
    print('Slytherin')
else:
    print('Who? ')
'''


# Using "match" instead of "if" conditonals 
name = input('What\'s your name? ')

'''
match name:
    case 'Harry':
        print('Griffyndor')
    case 'Hermione':
        print('Griffyndor')
    case 'Ron':
        print('Griffyndor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who? ')
'''


# "match" can be streamlined further using the "|" symbol to combine
        
match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print('Griffyndor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who? ')
    