# Question 1

def hollow_square(n): # We define the function
    result = ""
    row = 1 # This is the inisial row
    while row <= n:
        if row == 1 or row == n:
            result += '*' * n + '\n' 
        else:
            result += '*' + ' ' * (n - 2) + '*' + '\n'
        row += 1
    return result.strip() # We return the result

n = int(input("Enter the number of rows: ")) # User input
print(hollow_square(n)) # We call the function

# Question 2

def number_pattern(n): # We define the function
    result = ''
    row = 1
    while row <= n:
        number = 1
        line = ""
        while number <= row:
            line += str(number)
            number += 1
        result += line + '\n'
        row += 1
    return result.strip() # We return the result

n = int(input("Enter the number of rows: ")) # User input
print(number_pattern(n)) # We call the function

# Question 3

def sum_of_natural_numbers(n): # We define the function
    total = 0
    count = 1
    while count <= n:
        total += count
        count +=1
    return total # We return the sum

n = int(input("Enter the number: ")) # User input
print(f"The sum of all natural numbers is {sum_of_natural_numbers(n)}.") # We call the function

# Question 4

def centered_star_pyramid(n): # We define the function
    result = ""
    row = 1
    while row <= n:
        spaces = ' ' * (n - row)
        stars = '*' * (2 * row - 1)
        line = spaces + stars
        result += line
        if row != n:
            result += '\n'
        row += 1
    return result # We return the result

n = int(input("Enter the number of rows: ")) # User input
print(centered_star_pyramid(n)) # We call the function