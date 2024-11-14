# Bajaya Hare
# November 14, 2024
# P1 HW2
# Calculating Travel Expenses
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
gas= float(input('How much do you think you will spend on gas?'))
lodging= float(input('Approximately, how much will you need for accomodation/hotel?'))
food= float(input('Last, how much do you need for food?'))

result=(budget-gas-lodging-food)

print('-------Travel Expenses-------')
print('Location:',location)
print('Initial Budget:',budget)

print('Fuel:',gas)
print('Accomodation:',lodging)
print('Food:',food)

print('Remaining Balance:',result)

#Psedocode(logic)
