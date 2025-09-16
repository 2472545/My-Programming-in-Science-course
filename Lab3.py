import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).

def polar_to_cartesian(r, theta): # We define the function
    x = r*math.cos(math.radians(theta)) # Formula for x
    y = r*math.sin(math.radians(theta)) # Formula for y
    return (round(x,5),round(y,5)) # We tell the function to return (x, y)

r = float(input("What is the radius in the polar plane? ")) # User input
theta = float(input("What is the angle (in degrees) in the polar plane? ")) # User input
print(f"The coordinates are {polar_to_cartesian(r, theta)} in the cartesian plane.") # We call the function


# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).

def cartesian_to_polar(x, y): # We define the function
    r = math.sqrt(x**2 + y**2) # We set the formula for r
    theta = math.degrees(math.atan(y/x)) # We set the formula for theta
    return (round(r,5), round(theta,5)) # We tell the function to return (r, theta)

x = float(input("What is the x coordinate in the cartesian plane? ")) # User input
y = float(input("What is the y coordinate in the cartesian plane? ")) # User input
print(f"The coordinates are {cartesian_to_polar(x, y)} in the polar plane.") # We call the function

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.

def pendulum_position(A, f, phi, t): # We define the function
    x = A*math.cos(2*math.pi*f*t + math.radians(phi)) # formula for x
    return round(x, 5) # We tell the function to return the value for x

A = float(input("What is the amplitude (in metres)? ")) # User input
f = float(input("What is the frequency (in Hz) ? ")) # User input
phi = float(input("What is the phase constant (in degrees)? ")) # User input
t = float(input("what is the time (in seconds)? ")) # User input
print(f"The position of the pendulum is {pendulum_position(A, f, phi, t)} metres.") # We call the function
