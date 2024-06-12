#ZedShaw Python Exercise #15
# this is about file input and output!


# Ask the user for the file name
file_name = input("Enter the file name: ")

try:
    # Open the file
    with open(file_name) as file:
        # Read and print the file content
        print(f"The file {file_name} contains:")
        print(file.read())
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
