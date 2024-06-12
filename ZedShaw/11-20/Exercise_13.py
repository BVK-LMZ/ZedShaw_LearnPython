#ZedShaw Python Exercise #13
# this is about the difference between argv and Input

from sys import argv

script, age, weight, gender = argv

print("Based on your self-reported data:")
print(f"You are a {gender}, aged {age}, and weigh {weight} pounds.")


#python script.py 25 150 male
#^By using this we are able to set arguements before the program runs which is different from input()