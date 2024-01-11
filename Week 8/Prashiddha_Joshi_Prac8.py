#1
width = 104.32
height = 15.654
area = width * height
Area = f"The area of a rectangle with a width of {width} and a height of {height} is {area}."
print(Area)
# The area of a rectangle with a width of 104.32 and a height of 15.654 is 1633.0252799999998.

#2
width = 104.32
height = 15.654
area = width * height
Area = f"The area of a rectangle with a width of {width} and a height of {height} is {area:.3f}."
print(Area)
# The area of a rectangle with a width of 104.32 and a height of 15.654 is 1633.025.

#3
name= "prasijosi"
age=19
print(f"{name:15} - {age:10}")
# prasijosi       -         19

#4
name = "Prashiddha Joshi"
age = 19.7123
print(f"{name:>20} {age:$>20.2f}")
    # Prashiddha Joshi $$$$$$$$$$$$$$$19.71


#5
import math
r = 52
area = math.pi * r**2
area_of_circle = "Area of circle with a radius of {radius} is {area:.2f}.".format(radius=r, area=area)
print(area_of_circle)
# Area of circle with a radius of 52 is 8494.87.

#6
name = "Prashiddha Joshi"
age = 19
string_formatting = "{name:@^15} - {age:#^10}".format(name=name, age=age)
print(string_formatting)


