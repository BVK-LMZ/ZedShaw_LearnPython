# ZedShaw Python Exercise #32
# This Exercise is all about... LISTS


leather_bag = []
items_to_add = ["dagger", "apple", "map"]

# Initialize the leather_bag list with a loop
def innit_bag():
    for item in items_to_add:
        leather_bag.append(item)

# Define the function to print items in the bag with their indexes
def print_bag():
    for index, item in enumerate(leather_bag):
        print(f"{index}: {item}")

# Define the function to empty the bag
def empty_bag():
    while leather_bag:  # Loop until the bag is empty
        leather_bag.pop()  # Remove the last item from the bag

# Define the function to check if an item is in the bag
def is_item_in_bag(item_name):
    if item_name in leather_bag:
        print("true, item in bag")
    else:
        print("false, item not in bag")
        
#MAIN 
innit_bag() 
is_item_in_bag("map")
print("--")
print_bag()
print("---")
empty_bag()
print_bag()
    