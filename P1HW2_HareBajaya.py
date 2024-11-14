# Bajaya Hare
# November 14, 2024
# P1 HW2
# Calculating Travel Expenses

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
