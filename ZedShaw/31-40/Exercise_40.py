# ZedShaw Python Exercise #40
# # This Exercise is all about... Modules
# Modules are essentially libraries


# Simulated apples.py content
class Apples: # Define a dictionary in the simulated module
    def __init__(self):
        self.mystuff = {'apple': "Apples are awesome"}


#---------------------------------------------------------------------


# Main program functionality
if __name__ == "__main__":
    # Simulating the import of the apples module
    apples = Apples()
    
    # Access the dictionary from the simulated module and print it
    print(apples.mystuff)
