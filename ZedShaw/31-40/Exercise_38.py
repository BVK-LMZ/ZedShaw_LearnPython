# ZedShaw Python Exercise #38
# This Exercise is all about... ELEMENTS OF LISTS

# Make the list count to 10 without overiding the first 4 elements

some_list=[0,1,2,3]

for index in range (len(some_list),11):
    some_list.append(index)