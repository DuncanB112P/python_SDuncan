
x = int(input('What is x? '))
y = int(input('What is y? '))

'''
if x < y:
    print('x is less than y')
    
if x > y:
    print('x is greater than y')

if x == y:
    print('x is equal to y')
'''

##############################################################################

# use elif to ask less questions in the code

'''
if x < y:
    print('x is less than y')
    
elif x > y:
    print('x is greater than y')

elif x == y:
    print('x is equal to y')
'''
#############################################################################

# using else in logic
'''
if x < y:
    print('x is less than y')
    
elif x > y:
    print('x is greater than y')

else:
    print('x is equal to y')  # no need for a final question bc logic dictates 
                              # the response
'''                              
#############################################################################
'''
if x < y or x > y:
    print('x is not equal to y')
else:
    print('x is equal to y')
'''

#############################################################################

# If you are only concerned about the equality of one to another, the code can
# be streamlined further

if x != y:
    print('x is not equal to y')
else:
    print('x is equal to y')
    

