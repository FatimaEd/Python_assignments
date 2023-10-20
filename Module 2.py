#Module 2
name= input("what's your name: ")
print(f"Hello, {name}!")

#Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
from math import pi
radius= float(input("Enter circle radius: "))
area = pi * (radius ** 2)
print(f"The area of the circle is : {area}")

#Write a program that asks the user for the length and width of a rectangle.

length = float(input("Enter the length the rectangle: "))
width = float(input("Enter the width the rectangle: "))

area = length * width
perimeter = (length + width) * 2

print(f"The area of a rectangle is: {area}")
print(f"the perimeter of a rectangle is: {perimeter}")

#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

first_integer = int(input("Enter the first integer: "))
second_integer = int(input("Enter the second integer: "))
third_integer = int(input("Enter the third integer: "))

sum = first_integer + second_integer + third_integer
product = first_integer * second_integer * third_integer
average = sum / 3

print(f"The sum of the numbers is: {sum}")
print(f"The product of the numbers is: {product}")
print(f"The average of the numbers is: {average}")


#5
pound_per_talent = 20
lots_per_pound = 32
grams_per_lots = 13.3

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_grams = talents * pound_per_talent * lots_per_pound * grams_per_lots + pounds * lots_per_pound * grams_per_lots + lots * grams_per_lots

kilograms = int(total_grams // 1000)
grams = round(total_grams % 1000, 2)


print(f"The weight in modern units: {kilograms} kilograms and {grams} grams.")

#6- Write a program that draws two random combinations of numbers for a combination lock

import random

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random_list = random.sample(list, 3)
print(random_list)

sec_list = [0, 1, 2, 3, 4, 5, 6]
random_list = random.sample(sec_list, 4)
print(random_list)
