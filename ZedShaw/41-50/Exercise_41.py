# ZedShaw Python Exercise #41
# This Exercise is all about... CLASSES and key sytax!


# Define a class named Knight
class Knight:
    
    # Initialize the Knight object with hp (hit points) and dps (damage per second)
    def __init__(self, hp, dps):
        # Set the instance attribute hp to the value passed during object creation
        self.hp = hp
        # Set the instance attribute dps to the value passed during object creation
        self.dps = dps
    
    # Define a method named explore that belongs to the Knight class
    def explore(self):
        # Print a message indicating that the knight is exploring
        print("The Knight Walks Around")

# Create an instance of the Knight class with 100 hit points and 20 damage per second
my_knight = Knight(100, 20)

# Access and print the hp attribute of the my_knight object
print(f"Knight HP: {my_knight.hp}")
# Access and print the dps attribute of the my_knight object
print(f"Knight DPS: {my_knight.dps}")

# Call the explore method of the my_knight object
my_knight.explore()

