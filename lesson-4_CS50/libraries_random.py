# import the Random library
import random

#Create a variable coin and use the random.choice function to pass in the parameters heads and tails
coin = random.choice(["heads", "tails"])
print(coin)


# You can also use "from" the module to place the scope of the library into the working file

'''
from random import choice
coin = choice(["heads", "tails"])   # no need to use "random" in this method
print(coin)
'''
#####################################################################################################


# RANDINT -- get a random integer from a range

import random

number = random.randint(1,10)
print(number)


############################################################################################

# SHUFFLE

import random

cards = ['Jack', 'Queen', 'King', 'Ace', 'Ten']
random.shuffle(cards)
for card in cards:
    print(card)

