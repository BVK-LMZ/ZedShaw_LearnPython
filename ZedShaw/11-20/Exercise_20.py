#ZedShaw Python Exercise #20
# A remake of Exercise 15 but with functions!!

def get_file_name():
    """Prompt the user to enter a file name and return it."""
    return input("Enter the file name: ")

def read_file(file_name):
    """Read the contents of the file and return it."""
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

def display_file_content(file_name, content):
    """Display the content of the file or an error message if the file was not found."""
    if content is None:
        print(f"Error: File '{file_name}' not found.")
    else:
        print(f"The file {file_name} contains:")
        print(content)

def main():
    """Main function to run the file reading process."""
    file_name = get_file_name()
    content = read_file(file_name)
    display_file_content(file_name, content)

if __name__ == "__main__":
    main()
