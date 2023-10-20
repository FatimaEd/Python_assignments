""""#1.
import random

dice_number = int(input("How many times you want to roll the dice?"))
total = 0
for _ in range(dice_number):
    roll = random.randint(1,6)
    total += roll
print(f"The sum of {dice_number} dice rolls: {total}")

#2.

numbers = []

while True:
    user_input = input("Enter a number or press Enter to quit:")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid number, Please enter a valid number.")

numbers.sort(reverse=True)
top_five = numbers[:5]
print(f"The five greatest numbers in descending order: {top_five}")

#3.

number = int(input("Enter a integer: "))
if number <= 1:
    prime = False
else:
    prime = True
    i = 2

    while i * i <= number:
        if number % i == 0:
            prime = False
            break
        i += 1
if prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#4.
cities = []
for i in range(5):
    city_name = input(f"Enter a city name {i + 1}: ")
    cities.append(city_name)
print("Cities entered: ")
for city in cities:
    print(city)"""
