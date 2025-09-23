# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.

def built_in_functions_max(num1, num2, num3): # We define the function
    number_list = [num1, num2, num3] # We set the list
    maximum = max(number_list) # We use the python built in function: max
    return maximum # We want to return the maximum value
num1 = float(input("Enter the first number: ")) # User input
num2 = float(input("Enter the second number: ")) # User input
num3 = float(input("Enter the third number: ")) # User input
print(f"The maximum number is {built_in_functions_max(num1, num2, num3)}") # We call the function

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.

def built_in_functions_min(num1, num2, num3): # We define the function
    number_list = [num1, num2, num3] # We set the list
    minimum = min(number_list) # We use the python built in function: min
    return minimum # We want to return the minimum value
num1 = float(input("Enter the first number: ")) # User input
num2 = float(input("Enter the second number: ")) # User input
num3 = float(input("Enter the third number: ")) # User input
print(f"The minimum number is {built_in_functions_min(num1, num2, num3)}") # We call the function
    

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.

def check_number(number):
    if number == 0:
        return "Your number is 0"
    elif number < 0:
        return "Your number is negative"
    else:
        return "Your number is positive"
number = float(input("Enter your number: "))
print(check_number(number))
       

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    # TODO: Implement this function
    pass  # Replace with your code
    
# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    # TODO: Implement this function
    pass  # Replace with your code

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    # TODO: Implement this function
    pass  # Replace with your code
