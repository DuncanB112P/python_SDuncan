"""
x = input('What is x? ')
y = input('What is y? ')

z = int(x) + int(y)

print(x+y)

"""

##########################################################################

### Rather than separating the int function into a different cariable (z), 
### we can nest the int function with the input function.

"""
x = int(input('What is x? '))
y = int(input('What is y? '))

print(x + y)

"""
#########################################################################

#instead of converting to integers x and y, we can conver to a float

"""
x = float(input('What is x? '))
y = float(input('What is y? '))

print(x + y)

"""
#########################################################################

#Using the 'round' function 
# round(number[, ndigits])

"""
x = float(input('What is x? '))
y = float(input('What is y? '))

z = round(x + y)

print(f"{z:,}") #using format string to add the comma to large numbers 

"""

#########################################################################
'''
x = float(input('What is x? '))
y = float(input('What is y? '))

z = x / y 

print(f"{z:.2f}") #using the f string to round z to 2 decimal places

# can also be done with:


z = round(x/y, 2)
print(z)
'''
#########################################################################

