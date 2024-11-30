 #Bajaya Hare
 #November 26, 2024
 #P3 HW1
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules

#These needed to be float input statements and quotes weren't closed
mod_1 = float(input('Enter grade for Module 1:'))
mod_2 = float(input('Enter grade for Module 2:'))
mod_3 = float(input('Enter grade for Module 3:'))
mod_4 = float(input('Enter grade for Module 4:'))
mod_5 = float(input('Enter grade for Module 5:'))
mod_6 = float(input('Enter grade for Module 6:'))

# add grades entered to a list

numbers = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

min_value = min(numbers)
max_value = max(numbers)
gradesum = sum(numbers)
avg = sum(numbers)/len(numbers)

# determine letter grade for average
print('-------Results-------')
print(f"{'Lowest Grade:':<20} {min_value:.1f}")
print(f"{'Highest Grade:':<20} {max_value:.1f}")
print(f"{'Sum of Grades:':<20} {gradesum:.1f}")
print(f"{'Average:':<20} {avg:.2f}")
print('--------------------------------------------')

if avg >= 90:
    print('Your grade is: A')
#Add elif statements since there is multiple branches
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this





