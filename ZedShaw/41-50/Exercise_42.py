# ZedShaw Python Exercise #42
# This Exercise is all about... poop, python object orreinated programming2

#pay speical atention to this line below, for checking if the classes that inhert from knight do really inheret from knight
#SHOUOOOOOOOOOOOOOOOOOOOOOOOOOOOOOUT OUTTTTTTTTTTTTT

# Define the base class Knight
class Knight:
    
    # Initialize the Knight object with hp (hit points) and dps (damage per second)
    def __init__(self, hp, dps):
        self.hp = hp
        self.dps = dps
    
    # Define a method named explore that belongs to the Knight class
    def explore(self):
        print("The Knight Walks Around")

# Define the HolyKnight class, inheriting from Knight
class HolyKnight(Knight):
    
    # Initialize the HolyKnight object with the same attributes as Knight
    def __init__(self, hp, dps):
        # Call the constructor of the parent class (Knight) to initialize its attributes
        super().__init__(hp, dps)

# Define the DarkKnight class, inheriting from Knight
class DarkKnight(Knight):
    
    # Initialize the DarkKnight object with the same attributes as Knight
    def __init__(self, hp, dps):
        # Call the constructor of the parent class (Knight) to initialize its attributes
        super().__init__(hp, dps)

# Main function to create objects
def main():
    # Create instances of Knight, HolyKnight, and DarkKnight
    regular_knight = Knight(100, 20)
    holy_knight = HolyKnight(120, 25)
    dark_knight = DarkKnight(150, 30)
    
    # Access and print attributes of each knight
    print("Regular Knight:")
    print(f"HP: {regular_knight.hp}, DPS: {regular_knight.dps}")
    
    print("\nHoly Knight:")
    if isinstance(holy_knight, Knight): #SHOUOOOOOOOOOOOOOOOOOOOOOOOOOOOOOUT OUTTTTTTTTTTTTT
        print("This is indeed a Knight!")#SHOUOOOOOOOOOOOOOOOOOOOOOOOOOOOOOUT OUTTTTTTTTTTTTT
    print(f"HP: {holy_knight.hp}, DPS: {holy_knight.dps}")
    
    print("\nDark Knight:")
    if isinstance(holy_knight, Knight): #SHOUOOOOOOOOOOOOOOOOOOOOOOOOOOOOOUT OUTTTTTTTTTTTTT
        print("This is indeed a Knight!") #SHOUOOOOOOOOOOOOOOOOOOOOOOOOOOOOOUT OUTTTTTTTTTTTTT
    print(f"HP: {dark_knight.hp}, DPS: {dark_knight.dps}")
    
    # Call the explore method for each knight
    print("\nExploring...")
    regular_knight.explore()
    holy_knight.explore()
    dark_knight.explore()

# Call the main function if this script is run directly
if __name__ == "__main__":
    main()
