#Bajaya Hare
#11/19/2024
#P2LAB1
#Program makes circle calculations from the radius
import math
radius = float(input("What is the radius of the circle? "))
#Add import math to intergrate pi into the program
#Diameter = 2r
#Circumfurence= 2*pi*r
#Circle Area= pi*r^2
diameter = radius * 2
circumference = math.pi * radius * 2 
area = math.pi * radius * radius
#print out each calculation result
print("The diameter of the circle is ", diameter)
print("The circumference of the circle is ", circumference)
print("The area of the circle ", area)
