"""Declare age in string"""
age = 25

"""Declare height as a float variable"""
height = 5.3

"""Declare a variable that store a complex number"""
comp = 2 + 5j

import math


"""Script that prompts the user to enter base and height of the triangle and calculate an area of the triangle"""
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter hegiht of triangle: "))

area_triangle = 0.5 * base * height
print(f"The area of triangle is: {area_triangle}")


"""script that prompts the user to enter side a,b,c of the triangle. Calculate the perimeter of the triangle"""
side_a = float(input("Enter the value for side a of triangle:"))
side_b = float(input("Enter the value for side b of triangle:"))
side_c = float(input("Enter the value for side c of triangle:"))

perimeter = side_a + side_b + side_c
print(f"Perimeter of the triangle: {perimeter}")


"""Get length and width of a rectangle using prompt. Calculate its area and perimeter"""
length = float(input("Enter length of rect: "))
width = float(input("Enter width of rect: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area of rect: {area}")
print(f"Perimeter of rect: {perimeter}")


"""Get radius of a circle using prompt. Calculate the area and circumference"""
radius = float(input("Enter the radius of circle: "))
pi = 3.14
area = pi * (radius**2)
circumference = 2 * pi * radius

print(f"Area: {area}")
print(f"Circumference: {circumference}")


"""Calculate the slope, x-intercept and y-intercept of y = 2x -2"""

m = float(input("Enter slope value: "))
c = float(input("Enter y_intercept value:"))

if m != 0:
    x_intercept = -c/m
    print(x_intercept)

slp1 = m


""" Find the slope and Euclidean distance between point (2, 2) and point (6,10)"""
(x1, y1) = (2, 2)
(x2, y2) = (6, 10)

slp2 = (y2 - y1)/(x2 - x1)
euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Slope2: {slp2}")
print(f"Distance between two points: {euclidean_distance}")


"""Compare the slope in task 8 and 9"""
if slp1 == slp2:
    print(f"Both the slopes are equal")
else:
    print("Slopes are not equal")


"""Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and 
figure out at what x value y is going to be 0"""

print(f"{'X':>3} {'Y':>4}")
for x in range(-5, 6, 1):
    y = x**2 + 6*x +9
    print(f"{x:>3} {y:>4}")

# With function
def equation():
    print(f"{'X':>2} {'Y':>4}")
    for x in range(-5, 6, 1):
        y = x**2 + 6*x +9
        print(f"{x:>2} {y:>4}")
equation()

"""Find the length of 'python' and 'dragon' and make a falsy comparison statement."""
A = 'python'
B = 'dragon'

print('Length of python:', len(A))
print('length of dragon:', len(B))

print('len(python) != len(dragon):', len(A) is not len(B))
print('len(python) != len(dragon):',len(A) != len(B))


"""Use and operator to check if 'on' is found in both 'python' and 'dragon'"""

print('on' in 'python' and 'on' in 'dragon')

if 'on' in 'python' and 'dragon':
    print(True)
else:
    print(False)


"""I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence."""

print('jargon' in 'I hope this course is not full of jargon')


"""There is no 'on' in both dragon and python"""

print('on' not in 'python' and 'on' not in 'dragon')


"""Find the length of the text python and convert the value to float and convert it to string"""
program = len('python')
print(program)
len_float = float(program)
print(len_float)
len_str = str(program)
print(len_str)

"""How do you check if a number is even or not using python?"""
for i in range(10):
    if i % 2 == 0:
        print(f"The number {i} is even")
    else:
        print(f"The number {i} is odd")
# OR
i = int(input("Enter the number: "))
if i % 2 == 0:
    print("Even number")
else:
    print("Odd number")

"""Check if the floor division of 7 by 3 is equal to the int converted value of 2.7."""

num = int(2.7)
floor_division = 7 // 3
print(floor_division is num)


"""Check if type of '10' is equal to type of 10"""
a = '10'
b = 10
print(type(a) is type(b))


"""Check if int('9.8') is equal to 10"""
a = float('9.8')
b = int(a)
c = 10
print(b is c)


"""script that prompts the user to enter hours and rate per hour. Calculate pay of the person"""

hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
pay_person = hours * rate_per_hour
print('Your daily earnings:', pay_person)


"""script that prompts the user to enter number of years. Calculate the number of seconds a person can live."""

years = int(input("Enter number of years person lived: "))
sec = years * (365 * 24 * 60 * 60)
print('Number of sec person can live:', sec)


"""Python script that displays the following table"""
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
    # print(f"{i:>2} {1:>2} {i:>2} {i**2:>2} {i**3:>2}")  # with space between digits






