#Create an empty list for the Grocery List
GrocList = []

# Create a dictionary that will hold the item counter number and the item as a key/value pair
item_count = {}

while True:

    try:
        # Take user input and convert it to upper case, then append that input to the GrocList
        x = input().upper()
        GrocList.append(x)

        # If the user entry is already in the item_count, then increase the item and count for 
        # that item by 1. If it is not already there, then x is added to the item_count and the 
        # count for that item is 1
        if x in item_count:
            item_count[x] += 1
        else:
            item_count[x] = 1

    # Upon a KeyboardInterrupt (ctrl + C), break out of the loop
    except KeyboardInterrupt:
        break

# Create set (using set() function) that includes items in GrocList that is "sorted" (sort method default to alphabetical order)
# set() rejects duplicate values
unique_items = sorted(set(GrocList))

for item in unique_items:
    print(f"{item_count[item]} {item}")   

 







    


