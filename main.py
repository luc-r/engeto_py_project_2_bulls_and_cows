"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Lucie Robošová
email: lucka.robosova@gmail.com
"""



# ________________________________________________________________________________
# LIBRARIES

from random import sample
from time import time



# ________________________________________________________________________________
# CONSTANTS

line = "-" * 50



# ________________________________________________________________________________
# FUNCTION DEFINITIONS

# random 4 digit number generator (function)

def generate_random_number() -> str:
    """
    Generates a random 4-digit string with unique digits where the first digit is not zero.

    Returns:
        str: The generated 4-digit number as a string.
    """
    first_number = sample(range(1, 10), 1)[0]               # pick first number from 1 to 9
    numbers = list(range(0, 10))                    
    numbers.remove(first_number)                            # create a list of numbers from 0 to 9 without 1st number
    other_numbers = sample(numbers, 3)                      # pick 3 numbers from that list
    all_numbers_list = [first_number] + other_numbers       # create 1 list from all the numbers
    generated_number = "".join(map(str, all_numbers_list))  # create a string of 4 numbers from the list
    return generated_number



# user input checker (function)

def check_user_input(user_input: str) -> str | None:
    """
    Validates the user input string.

    The input is valid if:
    - All characters are digits.
    - It consists of exactly 4 characters.
    - The first digit is not zero.
    - Digits are unique (no duplicates).

    Parameters:
        user_input (str): User's input as a string.

    Returns:
        str: An error message if the input is invalid.
        None: If the input is valid.
    """
    if not user_input.isdigit():                                # only digits control
        return "Enter only digits."
    if len(user_input) != 4:                                    # input lenght control
        return "Enter a four-digit number."
    if user_input[0] == "0":                                    # not starting with 0 control
        return "Enter a number that does not start with zero."  
    if len(set(user_input)) != len(user_input):                 # unique digits control
        return "Enter unique, non-repeating digits."    
    return None



def count_bulls(user_input: str, generated_number: str) -> int:
    """
    Counts the number of bulls in the user's guess.
    A 'bull' is a correct digit in the correct position.

    Parameters:
        user_input (str): The user's guess as a 4-digit string.
        generated_number (str): The generated 4-digit number as string.

    Returns:
        int: Number of bulls.
    """
    bulls = sum(1 for i in range(4) if user_input[i] == generated_number[i])
    return bulls



def count_cows(user_input: str, generated_number: str) -> int:
    """
    Counts the number of cows in the user's guess.
    A 'cow' is a correct digit in the wrong position.

    Parameters:
        user_input (str): The user's guess as a 4-digit string.
        generated_number (str): The generated 4-digit number as string.
        
    Returns:
        int: Number of cows.
    """
    cows = 0
    for i in range(4):
        user_digit = user_input[i]
        if user_digit in generated_number and user_digit != generated_number[i]:
            cows += 1
    return cows



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



# the bulls and cows game

print("Enter a number: ")                               # instruction
print(line)



bulls = 0
time_start = None

while bulls != 4:
    user_input = input(">>> ")                          # user input

    error_message = check_user_input(user_input)        # check the correct user input format
    if error_message is not None:                       # continue the program if the input is valid
        print(error_message)                            # print error message on invalid input
        continue

    if time_start is None:                              # start time point
        time_start = time()

    bulls = count_bulls(user_input, generated_number)   # count number of bulls in guess
    cows = count_cows(user_input, generated_number)     # count number of cows in guess

    bulls_word = "bull" if bulls == 1 else "bulls"      # flexible name by number
    cows_word = "cow" if cows == 1 else "cows"

    print(f"{bulls} {bulls_word}, {cows} {cows_word}")  # show the count of bulls and cows in guess
    print(line)

time_end = time()                                       # end time point
time_elapsed = time_end - time_start                    # guessing time



print(f"Congratulations! You've guessed the right number in {time_elapsed:.1f} seconds.")
print(line)
print("Well done!")