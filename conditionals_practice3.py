# use the % symbol to refer to the remainder 
'''
x = int(input('What is x? '))
if x % 2 == 0:
    print('Even')
else:
    print('Odd')
'''



def main():
    x = int(input('What is x? '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')
        
''' 
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

'''
# a more succinct version of the "def is_even" function would be to 
# simply RETURN the statement [n % 2 == 0]. It will be read as either True
# or False, and if True (i.e. "if_even", then it will print "Even", else...)

def is_even(n):
    return n % 2 == 0

main()