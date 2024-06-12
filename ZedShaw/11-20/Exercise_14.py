#ZedShaw Python Exercise #14
# this focuses on using both ARGV and INPUT 

from sys import argv

script, age_from_argv = argv

# Prompt the user to confirm if they want to change the age
confirm_change = input(f"Your default age is {age_from_argv}. Do you want to change it? (T/F) ")

if confirm_change.lower() == 't':
    age_from_input = input("Enter your age: ")
    age = age_from_input if age_from_input else age_from_argv
else:
    age = age_from_argv

print(f"Your final age is {age}.")
