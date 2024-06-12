# ZedShaw Python Exercise #31
# This Exercise is all about... Implementing if else

def single_door_game():
    print("You are standing in front of a door.")
    choice = input("Do you want to enter the room behind the door? (yes/no)\n>").lower()

    if choice == 'yes':
        print("You entered the room and encountered a bear. You were mauled. Game over.")
    elif choice == 'no':
        print("You decided not to enter the room. Game over.")
    else:
        print("Invalid choice. Game over.")

single_door_game()
