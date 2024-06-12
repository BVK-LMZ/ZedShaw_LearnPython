#ZedShaw Python Exercise #18
# Introduction to FUNCTIONS

def get_user_data():
    script = input("Enter your script: ")
    age = input("Enter your age: ")
    weight = input("Enter your weight in pounds: ")
    gender = input("Enter your gender: ")
    return script, age, weight, gender

def print_user_data(script, age, weight, gender):
    print("Based on your self-reported data:")
    print(f"You are a {gender}, aged {age}, and weigh {weight} pounds.")
    print("Your script is:", script)

def run_program():
    script, age, weight, gender = get_user_data()
    print_user_data(script, age, weight, gender)

run_program()
