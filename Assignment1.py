# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.

def built_in_functions_max(num1, num2, num3): # We define the function
    maximum = max(num1, num2, num3) # We use the max function
    return maximum # We return the maxumum value
num1 = int(input("Enter the first number: ")) # User input
num2 = int(input("Enter the second number: ")) # User input
num3 = int(input("Enter the third number: ")) # User input
print(f"The maximum number is {built_in_functions_max(num1, num2, num3)}") # We call the function


# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.

def built_in_functions_min(num1, num2, num3): # We define the function
    minimum = min(num1, num2, num3) # We use the min function
    return minimum # We return the minimum value
num1 = int(input("Enter the first number: ")) # User input
num2 = int(input("Enter the second number: ")) # User input
num3 = int(input("Enter the third number: ")) # User input
print(f"The minimum number is {built_in_functions_min(num1, num2, num3)}") # We call the function
    

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.

def check_number(number): # We define the function and set conditions below
    if number == 0: 
        return "Your number is 0" # We return a string
    elif number < 0: 
        return "Your number is negative" # We return a string
    else: 
        return "Your number is positive" # We return a string
number = float(input("Enter your number: ")) # User input
print(check_number(number)) # We call the function
       

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.

def star_shape(rows): # We define the function
    for x in range(1, rows + 1): # We use the for loop and range function
        print("*" * x) # This will print rows of stars to form a triangle
rows = int(input("How many rows does the triangle have? ")) # User input
star_shape(rows) # We call the function

    
# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".

def count_multiples_of_3(limit):
    x = 1 # We set the starting number in the while loop
    while x <= limit: # We set the condition for the while loop 
        if x % 3 == 0: # We set a condition in the loop
            print("Multiple of 3!") # We set our output
        else: # We set another condition in the loop
            print(x) # We set our output
        x += 1 # We set this so the loop does not go on forever
           
limit = int(input("Enter the limit: ")) # User input
count_multiples_of_3(limit) # We call the function


# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end): # We define the function
    total = 0 # This is the intial sum (no values)
    for x in range(start, end + 1): # We set the for loop
        if x % 2 == 0:
            total += x # This is necessary for this loop to function
    print(f"The sum is {total}!") # We set our output
start = int(input("What is the starting number? ")) # User input
end = int(input("What is the ending number? ")) # User input
sum_of_even_numbers(start, end) # We call the function
