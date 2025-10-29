# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.

def remove_duplicates_and_sort(numbers): # We define the function
    duplicates_removed = set(numbers) # We use the python built in set() function which removes the duplicates https://www.w3schools.com/python/ref_func_set.asp
    sorted_list = sorted(duplicates_removed) # We use the python built in sorted() function which sorts the numbers https://www.w3schools.com/python/ref_func_sorted.asp
    return sorted_list # We return the sorted list with duplicates removed

numbers = [1, 6, -5, -5, 6, 3, 8, 20, 104, 103, 26, 57, -800, -789, 3, -5] # This is our list
print(remove_duplicates_and_sort(numbers)) # We call the function

#____________________________________________________________________________________________________________________

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr): # We define the function
    return []

#____________________________________________________________________________________________________________________


# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(my_list, step): # We define the function
    sliced_element = my_list[::step] # We use :: to slice by step https://www.geeksforgeeks.org/python/python-list-slicing/
    return sliced_element # We return the elements that were sliced out in a new list
step = 3 # This is our step
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26 ,27, 28, 29, 30] # This is our list
print(slice_every_nth(my_list, step)) # We call the function

#____________________________________________________________________________________________________________________

# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.

def dot_product(list1, list2): # We define the function
    array_multiplication = [a * b for a, b in zip(list1, list2)] # We use the zip() function to multiply the corresponding elements in list 1 and list 2 https://github.com/azharhanif/My-Programming/blob/main/lectures/Lecture%207%20-%20Lists%20and%20Arrays.md
    dot_product_result = sum(array_multiplication) # We use the sum() function to add the elements resulting from the array multiplication https://openstax.org/books/introduction-python-programming/pages/9-3-common-list-operations
    return dot_product_result # We return the result

list1 = [1, 2, 3, 4, 5] # This is our list 1
list2 = [6, 7, 8, 9, 10] # This is our list 2
print(dot_product(list1, list2)) # We call the function

# ___________________________________________________________________________________________________________________

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.

def matrix_multiplication(matrix1, matrix2): # We define the function
    result = [ [0, 0] ,  # We start with an empty matrix of zeros
               [0, 0] ]
    for i in range(len(matrix1)): # For i associated with matrix 1 
        for j in range(len(matrix2[0])): # For j associated with matrix 2 
            for k in range(len(matrix1)): # For k iassociated with matrix 1
                result[i][j] += matrix1[i][k] * matrix2[k][j] # We set our result
    return result # We return the result

matrix1 = [ [8, 9] ,     # We create matrix 1
            [7, 2] ]

matrix2 = [ [7, 1] ,     # We create matrix 2
            [2, 8] ]

print(matrix_multiplication(matrix1, matrix2)) # We call the function

# Steps taken from: https://openstax.org/books/introduction-python-programming/pages/9-4-nested-lists
