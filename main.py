"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Lucie Robošová
email: lucka.robosova@gmail.com
"""



# ________________________________________________________________________________
# LIBRARIES

from random import sample



# ________________________________________________________________________________
# CONSTANTS

line = "-" * 50



# ________________________________________________________________________________
# FUNCTION DEFINITIONS

# random 4 digit number generator (function)

def generate_random_number():
    """
    This function creates a four-digit string with unique numbers not starting with 0.
    """
    first_number = sample(range(1, 10), 1)[0]               # pick first number from 1 to 9
    numbers = list(range(0, 10))                    
    numbers.remove(first_number)                            # create a list of numbers from 0 to 9 without 1st number
    other_numbers = sample(numbers, 3)                      # pick 3 numbers from that list
    all_numbers_list = [first_number] + other_numbers       # create 1 list from all the numbers
    generated_number = "".join(map(str, all_numbers_list))  # create a string of 4 numbers from the list
    return generated_number



# user input checker (function)

def check_user_input(user_input: str):
    """
    This function checks whether the user input has the correct format 
    - whether it is exactly 4 digits, does not contain duplicates, does 
    not start with a zero, and does not contain non-digit characters.

    If there is an error in the input, it returns an error message. 
    If the input is OK, it returns no value.
    """
    if len(user_input) != 4:                                    # input lenght control
        return "Enter a four-digit number."
    if len(set(user_input)) != len(user_input):                 # unique digits control
        return "Enter unique, non-repeating digits."
    if user_input[0] == "0":                                    # not starting with 0 control
        return "Enter a number that does not start with zero."      
    if not user_input.isdigit():                                # only digits control
        return "Enter only digits."
    return None



# ________________________________________________________________________________
# MAIN PROGRAM

# random 4-digit number generation

generated_number = generate_random_number()



# introduction

print("Hi there!")
print(line)
print("""
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Guess the 4 digit number!
""".strip())
print(line)



# user input

while True:
    user_input = input("Enter a number: ")
    error_message = check_user_input(user_input)    # check the correct user input format
    if error_message is None:                       # continue the program if the input is valid
        break
    print(error_message)                            # print error message on invalid input

print(line)