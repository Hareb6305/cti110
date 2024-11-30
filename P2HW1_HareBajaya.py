# Bajaya Hare
# November 26, 2024
# P2 HW1
# Calculating Travel Expenses + adding f-strings
#
#*****pseudocode****
#Ask user to enter their budget
#Ask user to enter travel destination
#Ask user for amount they will spend on gas
#Ask user for amount they will spend on accommodation
#Ask user for amount they will spend on food
#Add expenses
#Subtract expenses from budget
#Display results

print('This program calculates and displays travel expenses')

budget= float(input('Enter budget:'))
location=input('Enter your travel destination:')
gas= float(input('How much do you think you will spend on gas?' ))
lodging= float(input('Approximately, how much will you need for accomodation/hotel?'))
food= float(input('Last, how much do you need for food?'))

result=(budget-gas-lodging-food)
#Add f-strings
#Add .2f for the two decimal points
#You're suppose to add :<20 after each print before the variables to make the data right aligned
#Example: print(f"{'Budget:' :<20} ${budget:.2ft}")
print('-------Travel Expenses-------')
print(f"{'Location:':<20} {location}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")

print(f"{'Fuel:':<20} ${gas:.2f}")
print(f"{'Accomodation:' :<20} ${lodging:.2f}")
print(f"{'Food:' :<20} ${food:.2f}")
print('-----------------------------')
print(f"{'Remaining Balance:' :<20} ${result:.2f}")




