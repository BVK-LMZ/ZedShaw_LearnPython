#ZedShaw Python Exercise #16
# This will load a file clear it, and then write to it

# Ask the user for the file name
file_name = input("Enter the file name: ")

try:
    # Open the file in write mode to erase its contents
    with open(file_name, 'w') as file:
        # Erase the contents of the file
        file.truncate(0)
    print(f"Contents of the file '{file_name}' erased successfully.")

    # Ask the user for two lines to write to the file
    line1 = input("Enter the first line: ")
    line2 = input("Enter the second line: ")

    # Open the file in append mode to add the new lines
    with open(file_name, 'a') as file:
        # Write the new lines to the file
        file.write(line1 + '\n')
        file.write(line2 + '\n')

    print("Lines written to the file successfully.")
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
