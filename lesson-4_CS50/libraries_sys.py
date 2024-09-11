
'''
import sys

try:
    print('Hello, my name is', sys.argv[1])
except IndexError:
    print('Error: Too few arguments')
'''
# Another option rather than trying exceptions
'''
import sys

if len(sys.argv) < 2:
    print('Error: too few arguments')
elif len(sys.argv) > 2:
    print('Error: too many arguments')
else:
    print('Hello, my name is', sys.argv[1])
'''

#####################################################################################################

# another way for error checking --> exiting the program using sys.exit if there conditional response 
# is not the desired response
'''
import sys

# Check for errors (the s"sys.exit" function lets us separate the error checking from the rest of code)

if len(sys.argv) < 2:
    sys.exit('Error: too few arguments')
elif len(sys.argv) > 2:
    sys.exit('Error: too many arguments')


# Execute code

print('Hello, my name is', sys.argv[1])
'''
#####################################################################################################

import sys

# Check for errors (the s"sys.exit" function lets us separate the error checking from the rest of code)

if len(sys.argv) < 2:
    sys.exit('Error: too few arguments')

for arg in sys.argv[1:]:    # The [1:] creates a slice of the list that starts at index 1 and goes until the end (no 2nd number)
    print('Hello, my name is', arg)
