# ZedShaw Python Exercise #35
# This Exercise is all about... BRANCHES & FUNCTIONS

#go on a journey through a few rooms
#go right both times to WIN!

def print_processing():
    print("PROCESSING")

def bear_room():
    print("You were mauled by a bear, gg")
    print("YOU LOSE")
    return False

def victory_room():
    print("You win!")
    return True

def choose_door(prompt):
    return input(prompt + " L/R?\n >")

def first_door():
    choice = choose_door("Do you want to go to the room on the")
    print_processing()
    
    if choice == "L":
        return bear_room()
    elif choice == "R":
        return second_door()
    else:
        print("Invalid choice")
        return first_door()

def second_door():
    choice = choose_door("Another door, do you want to go to the room on the")
    print_processing()
    
    if choice == "L":
        return bear_room()
    elif choice == "R":
        return victory_room()
    else:
        print("Invalid choice")
        return second_door()

def Door1():
    is_alive = first_door()
    return is_alive

if __name__ == "__main__":
    alive = Door1()
    if alive:
        print("Congratulations! You survived the game.")
    else:
        print("Game over. Better luck next time.")

