#Bajaya Hare
#November 30, 2024
#P3 HW2
#Evaluating whether an employee is working overtime and calculate what they're owed
#Input the employee's name, hours worked, and their pay rate
Employee_name = input("Enter employee's name:")
Work_hours = float(input("Enter number of hours worked:"))
Pay_rate = float(input("Enter employee's pay rate:"))
#Calculate the overtime pay using if-else statement
#Any number that exceeds 40 has overtimepay
#The overtime rate is 1.5
#The overtime pat would be overtime hours x the pay rate x 1.5
if Work_hours > 40:
    overtime_hours = Work_hours - 40
    overtime_pay = overtime_hours * Pay_rate * 1.5
    regular_pay = Work_hours * Pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = Work_hours * Pay_rate
#The gross pay is regular pay added with the overtime pay
gross_pay = regular_pay + overtime_pay

print("-------------------------------")
print(f" Employee name: {Employee_name}")
print("Hours Worked   Pay Rate  OverTime  OverTime Pay   RegHour Pay   Gross Pay")
print("--------------------------------------------------------------------------------")
print(f"{Work_hours:<15.2f}{Pay_rate:<10.2f}{overtime_hours:<10.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}")
