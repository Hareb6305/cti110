#Bajaya Hare
#November 30, 2024
#P3 HW2
#Calculate Gross Pay of Multiple Employees
##Ask user to enter another employee's name to calculate salary
#or "Done" to terminate program.
#Input the employee's name, hours worked, and their pay rate

Employee_name = input("Enter employee's name or \"Done\" to terminate:")

name_count = 0
total_overtime = 0.00
total_regular = 0.00
total_gross = 0.00

while Employee_name != "Done": #Add decision loop
    name_count +=1
    Work_hours = float(input("Enter number of hours worked:"))
    Pay_rate = float(input("Enter employee's pay rate:"))
    
    #Calculate the overtime pay using if-else statement
    #Any number that exceeds 40 has overtimepay
    #The overtime rate is 1.5
    #The overtime pat would be overtime hours x the pay rate x 1.5
    
    if Work_hours > 40:
        overtime_hours = Work_hours - 40
        
        overtime_pay = overtime_hours * Pay_rate * 1.5
        total_overtime += overtime_pay
        regular_pay = Work_hours * Pay_rate
        total_regular += regular_pay
    else:
        overtime_hours = 0
        overtime_pay = 0
        total_overtime += overtime_pay
        regular_pay = Work_hours * Pay_rate
        total_regular += regular_pay
        
    #The gross pay is regular pay added with the overtime pay
    ## Add 'total_gross += gross_pay
    gross_pay = regular_pay + overtime_pay
    total_gross += gross_pay
    print("-------------------------------")
    print(f" Employee name: {Employee_name}")
    print("Hours Worked   Pay Rate  OverTime  OverTime Pay   RegHour Pay   Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{Work_hours:<15.2f}{Pay_rate:<10.2f}{overtime_hours:<10.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}")
    Employee_name = input("Enter employee's name or \"Done\" to terminate:")
    
print(f"\nTotal number of employees entered: {name_count}")
print(f"Total amount paid for overtime:${total_overtime}")
print(f"Total amount paid for regular hours:${total_regular}")
print(f"Total amount paid in gross:${total_gross}")
