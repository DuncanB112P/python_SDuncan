'''
score = int(input('Score: '))

if score >= 90 and score <= 100:
    print('Grade: A')
elif score >= 80 and score < 90:
    print('Grade: B')
elif score >= 70 and score < 80:
    print('Grade: C')
elif score >= 60 and score < 70:
    print('Grade: D')
else:
    print('Grade: F')
'''

# Simplified
'''
if 90 <= score <= 100:
    print('Grade: A')
elif 80 <= score <= 90:
    print('Grade: B')
elif 70 <= score <= 80:
    print('Grade: C')
elif 60 <= score <= 70:
    print('Grade: D')
else:
    print('Grade: F')
'''


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
