# Bajaya Hare
# 11/21/2014
# P2 LAB2
# Creating a dictionary

#Keys are the automobile and The value is mpg

# Step 1: Create the dictionary with vehicle names as keys and MPG values as values
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Step 2: Prompt the user to enter a vehicle name
vehicle = input("Enter the vehicle to see it's mpg: ")

# Check if the entered vehicle is in the dictionary
if vehicle in vehicle_mpg:
# Step 3: Display the MPG for the entered vehicle
    mpg = vehicle_mpg[vehicle]
print(f"The {vehicle} gets {mpg}.")

# Step 4: Prompt the user to enter the number of miles they plan to drive
miles = float(input("How many miles will you drive the "+vehicle+" ?:"))

# Step 5: Calculate the gallons of gas needed
gallons_needed = miles / mpg

# Step 6: Display the gallons of gas needed, rounded to two decimal places
print(f"{gallons_needed:.2f} gallon(s) of gas are need to drive the {vehicle} {miles} miles.")



#create dictionary
