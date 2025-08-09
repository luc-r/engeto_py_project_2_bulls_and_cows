"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Lucie Robošová
email: lucka.robosova@gmail.com
"""



# libraries

from random import sample



# separator

line = "-" * 50



# random number generator

first_number = sample(range(1, 10), 1)[0]               # pick first number from 1 to 9

numbers = list(range(0, 10))                    
numbers.remove(first_number)                            # create a list of numbers from 0 to 9 without first number
other_numbers = sample(numbers, 3)                      # pick 3 numbers from that list

all_numbers_list = [first_number] + other_numbers       # create 1 list from all the numbers

generated_number = "".join(map(str, all_numbers_list))  # create a string of 4 numbers



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

user_input = int(input("Enter a number: "))
print(line)