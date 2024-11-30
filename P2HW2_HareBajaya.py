 #Bajaya Hare
 #November 26, 2024
 #P2 HW2
 #Creating Lists of Grades for each Module

#Ask user to enter grade of each Module

Module1= float(input('Enter grade for Module 1:'))
Module2= float(input('Enter grade for Module 2:'))
Module3= float(input('Enter grade for Module 3:'))
Module4= float(input('Enter grade for Module 4:'))
Module5= float(input('Enter grade for Module 5:'))
Module6= float(input('Enter grade for Module 6:'))
#Each of the Module variable is assigned as numbers
#Need to get the highest and lowest numbers using min and max functions
#Get the sum of grades using the sum(numbers)function
#Find the average of all grades using sum(numbers)/(len)numbers
numbers = [Module1, Module2, Module3, Module4, Module5, Module6]
min_value = min(numbers)
max_value = max(numbers)
gradesum = sum(numbers)
average = sum(numbers)/len(numbers)
#All of the results are f-strings
#:<20 is put in the the parenthesis before the variable to make it left aligned
#:.1f is put after the variables of min_value, max_value,& gradesum to be for the number to have 1 decimal number
print('-------Results-------')
print(f"{'Lowest Grade:':<20} {min_value:.1f}")
print(f"{'Highest Grade:':<20} {max_value:.1f}")
print(f"{'Sum of Grades:':<20} {gradesum:.1f}")
print(f"{'Average:':<20} {average:.2f}")
print('--------------------------------------------')
