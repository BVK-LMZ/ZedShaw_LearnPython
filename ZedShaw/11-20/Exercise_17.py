# ZedShaw Python Exercise #17
# This is about cloning a file

# Ask the user for the file name
file_name = input("Enter the file name: ")

try:
    # Open the file
    with open(file_name) as file:
        # Read and print the file content
        print(f"The file {file_name} contains:")
        print(file.read())

    # Ask for the name of the cloned file
    cloned_file_name = input("Enter the name for the cloned file: ")

    # Ensure the cloned file has a .txt extension
    if not cloned_file_name.endswith('.txt'):
        cloned_file_name += '.txt'

    # Open the original file again
    with open(file_name) as original_file:
        # Read the content of the original file
        file_content = original_file.read()

        # Create the cloned file with the user-specified name
        with open(cloned_file_name, 'w') as cloned_file:
            # Write the content of the original file to the cloned file
            cloned_file.write(file_content)

    print(f"File '{cloned_file_name}' cloned successfully!")
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
