#ZedShaw Python Exercise #24
#  So more practice of the fundamentals....
# INSTEAD lets use python practically to create a bunch of practice files for the rest of the book!

import os

# Define the directory where you want to create the files
directory = "exercise_files"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create files named "Exercise_x.py" where x ranges from 25 to 50
for i in range(25, 51):
    filename = f"{directory}/Exercise_{i}.py"
    with open(filename, 'w') as f:
        f.write(f"# Exercise {i}\n\n")
        f.write("# Write your Python code here")

print("Files created successfully!")
