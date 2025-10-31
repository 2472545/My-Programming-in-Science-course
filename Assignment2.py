# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.

def remove_duplicates_and_sort(numbers): # We define the function
    duplicates_removed = list(set(numbers)) # We make this variable a list of numbers with duplicates removed
    duplicates_removed.sort() # We sort our list
    return duplicates_removed # We return the sorted list with duplicates removed

numbers_list = [1, 6, -5, -5, 6, 3, 8, 20, 104, 103, 26, 57, -800, -789, 3, -5, -3, 8, -5, -1000] # This is our list
print(remove_duplicates_and_sort(numbers_list)) # We call the function

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.

def cumulative_sum(arr): # We define the function
    result = [] # We set an empty list as the result
    total = 0 # We set the total of the sum equal to zero
    for numbers in arr: # For loop
        total += numbers # We add the numbers to the total
        result.append(total) # We 'append' the total in a new list
    return result # We return the result

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] # This is our array
print(cumulative_sum(arr)) # We call the function

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(my_list, step): # We define the function
    sliced_element = my_list[::step] # We use :: to add a step to the slicing and we insert the step variable. It starts at index 0.
    return sliced_element # We return the elements that were sliced out in a new list
step = 3 # This is our step
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 ,27, 28, 29, 30] # This is our list
print(slice_every_nth(my_list, step)) # We call the function

# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.

def dot_product(list1, list2): # We define the function
    array_multiplication = [a * b for a, b in zip(list1, list2)] # We use the zip() function to multiply the corresponding elements in list 1 and list 2
    dot_product_result = sum(array_multiplication) # We use the sum() function to add the elements in the new array 
    return dot_product_result # We return the result of the sum

list1 = [1, 2, 3, 4, 5] # This is our list 1
list2 = [6, 7, 8, 9, 10] # This is our list 2
print(dot_product(list1, list2)) # We call the function

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.

def matrix_multiplication(matrix1, matrix2): # We define the function
    result = [ [0, 0] ,  # We start with an empty matrix of zeros
               [0, 0] ]
    for i in range(len(matrix1)): # For i associated with matrix 1 
        for j in range(len(matrix2[0])): # For j associated with matrix 2 
            for k in range(len(matrix1)): # For k associated with matrix 1
                result[i][j] += matrix1[i][k] * matrix2[k][j] # We set our result
    return result # We return the result

matrix1 = [ [8, 9] ,     # We create matrix 1
            [7, 2] ]

matrix2 = [ [7, 1] ,     # We create matrix 2
            [2, 8] ]

print(matrix_multiplication(matrix1, matrix2)) # We call the function
