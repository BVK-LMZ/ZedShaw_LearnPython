# ZedShaw Python Exercise #44
# This Exercise is all about... Inheritance VS Composition 


#Inheritance is suitable when there is a clear hierarchical relationship between classes 
# and when you want to model an "is-a" relationship (e.g., a Dog is-an Animal).

#Composition is preferable when you want to build objects dynamically, reuse code in a more flexible manner,
#  or model a "has-a" relationship (e.g., a Car has-an Engine).






# Summary:
# This program demonstrates the concepts of inheritance and composition in object-oriented programming.
# It defines classes for animals, specifically a base class Animal and derived classes Dog and Cat.
# Additionally, it shows composition with classes Engine and Car, where a Car object has an Engine object as a component.

# Base class Animal
class Animal:
    # Constructor to initialize species
    def __init__(self, species):
        self.species = species
    
    # Method to make a generic sound (to be overridden in subclasses)
    def make_sound(self):
        pass

# Derived class Dog inheriting from Animal
class Dog(Animal):
    # Constructor calls base class constructor with 'Dog' species
    def __init__(self):
        super().__init__('Dog')
    
    # Override method to make a specific sound for Dog
    def make_sound(self):
        print("Woof!")

# Derived class Cat inheriting from Animal
class Cat(Animal):
    # Constructor calls base class constructor with 'Cat' species
    def __init__(self):
        super().__init__('Cat')
    
    # Override method to make a specific sound for Cat
    def make_sound(self):
        print("Meow!")

# Class Engine representing an engine component
class Engine:
    # Method to start the engine
    def start(self):
        print("Engine started")

# Class Car representing a car with an Engine component
class Car:
    # Constructor initializes Car with an Engine object
    def __init__(self):
        self.engine = Engine()
    
    # Method to start the car (delegates to the Engine object)
    def start(self):
        self.engine.start()

# Main function to demonstrate inheritance and composition
def main():
    # Create instances of Dog and Cat
    dog = Dog()
    cat = Cat()

    # Call make_sound method for Dog and Cat
    print("Dog makes a sound:")
    dog.make_sound()
    print("\nCat makes a sound:")
    cat.make_sound()

    # Create instance of Car and start it
    print("\nStarting the car:")
    my_car = Car()
    my_car.start()

# Entry point of the program
if __name__ == "__main__":
    main()
