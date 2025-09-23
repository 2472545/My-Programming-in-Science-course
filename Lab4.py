# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def check_weekday_or_weekend(day_number): # We establish the function
    if 0 < day_number <6: # We set the conditions for weekdays
        return "Today is a weekday!"
    elif day_number == 6 or day_number == 7: # We set the conditions for weekends
        return "Today is a weekend!"
    else: # We set the conditions for invalid day numbers
        return "Invalid day number!"

day_number = int(input("What is the day number for today? ")) # User input
print(check_weekday_or_weekend(day_number)) # We call the function

# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_name(day_number): # We establish the function
    if day_number == 1: # We establish conditions for all days below
        return "Today is Monday!"    
    elif day_number == 2:
        return "Today is Tuesday!"
    elif day_number == 3:
        return "Today is Wednesday!"
    elif day_number == 4:
        return "Today is Thursday!"
    elif day_number == 5:
        return "Today is Friday!"
    elif day_number == 6:
        return "Today is Saturday!"
    elif day_number == 7:
        return "Today is Sunday!"
    else:
        return "Invalid day number!"

day_number = int(input("What is the day number for today? ")) # User input
print(get_day_name(day_number)) # We call the function