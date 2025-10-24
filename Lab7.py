# Function 1: Rotate the Array
# This function creates an array of a specified size, fills it with numbers starting from `starting_integer` and increasing by 3,
# then rotates elements at even indices 2 positions to the left.

def rotate_the_array(array_size, starting_integer): # We define the function
    the_array = [0] * array_size # Empty array
    for i in range(array_size): # This loop will iterate over the array size
        the_array[i] = starting_integer + i * 3 # Seperate all elements by 3
    for i in range(0, array_size - 2, 2): # This loop will iterate over the array size with increments of 2
        temp = the_array[i] # Temporary variable 
        the_array[i] = the_array[i + 2] # Move even elements two positions behind
        the_array[i + 2] = temp # The new elements are at the i'th place
    return the_array # We return the new array

array_size = int(input("Enter the array size: ")) # User input
starting_integer = int(input("What is the starting integer: ")) # User input
print(rotate_the_array(array_size, starting_integer)) # We call the function
