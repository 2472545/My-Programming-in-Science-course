# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.

def built_in_functions_max(num1, num2, num3): # We define the function
    number_list = [num1, num2, num3] # We set the list
    maximum = max(number_list) # We use the python built in function: max
    return maximum # We want to return the maximum value
num1 = int((input("Enter the first number: "))) # User input
num2 = int(input("Enter the second number: ")) # User input
num3 = int(input("Enter the third number: ")) # User input
print(f"The maximum number is {built_in_functions_max(num1, num2, num3)}") # We call the function

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.

def built_in_functions_min(num1, num2, num3): # We define the function
    number_list = [num1, num2, num3] # We set the list
    minimum = min(number_list) # We use the python built in function: min
    return minimum # We want to return the minimum value
num1 = int(input("Enter the first number: ")) # User input
num2 = int(input("Enter the second number: ")) # User input
num3 = int(input("Enter the third number: ")) # User input
print(f"The minimum number is {built_in_functions_min(num1, num2, num3)}") # We call the function
    

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.

def check_number(number): # We define the function
    if number == 0: # We set the first condition
        return "Your number is 0" # We return a string
    elif number < 0: # We set the second condition
        return "Your number is negative" # We return a string
    else: # If none of the above conditions are respected
        return "Your number is positive" # We return a string
number = float(input("Enter your number: ")) # User input
print(check_number(number)) # We call the function
       

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.

def star_shape(rows): # We define the function
    for x in range(1, rows + 1): # We use the for loop and the range function, setting the bounds for the range
        print("*" * x) # This will print rows of stars to form a triangle
rows = int(input("How many rows does the triangle have? ")) # We ask the user how many rows the triangle will have
star_shape(rows) # We call the function
    
# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".

def count_multiples_of_3(limit):
    x = 1 # We set the starting number in the while loop
    while x <= limit: # We set the condition for the while loop to continue
        if x % 3 == 0: # Within the original condition of the while loop, se set another condition 
            print("Multiple of 3!") # We set our output
        else: # Within the original condition of the while loop, se set another condition
            print(x) # We set our output
        x += 1 # We set this so the loop does not go on forever
           
limit = int(input("Enter the limit: ")) # We ask the user to enter the limit
count_multiples_of_3(limit) # We call the function

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end): # We define the function
    sum = 0 # This is the intial sum (no values)
    for x in range(start, end + 1): # We set the for loop
        sum += x # This is necessary for this loop to function
    print(f"The sum is {sum}!") # We set our output
start = int(input("What is the starting number? ")) # We ask the user to enter the starting number
end = int(input("What is the ending number? ")) # We ask the user to enter the ending number
sum_of_even_numbers(start, end) # We call the function
