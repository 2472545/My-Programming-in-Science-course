# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    g = 9.8 # We first define in the function the value of g (the gravitational acceleration constant)
    result1 = h0 - 1/2*g*t**2 #We then define the operation
    return result1

h0 = float(input("What is the initial height of the ball (in metres)? ")) #The input asks the user to put in the initial height
t = float(input("What is the time at which the height is calculated? ")) #The input asks the user to put in the time 
print(f"The height of the ball at the time {t} seconds is {calculate_height(h0, t)} metres.") #This output calls the function
# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    result2 = 20*t
    return result2
t = float(input("What is the time at which we need to know the distance travelled by the car (in seconds)? ")) #The input asks the user to put in the time
print(f"The distance traveled by the car at time {t} seconds is {calculate_car_distance(t)} metres. ") #This output calls the function