""""#1.
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#2.
inches = float(input("Enter how many inches you want to convert: "))

inches_to_cm = 2.54
while inches >= 0:
    centimeters = inches * inches_to_cm
    print(f"{inches} in = {centimeters} cm")
    inches = float(input("Enter another number to calculate, enter a negative number to end: "))
print("end")

#3.
numbers = []
while True:
    number_input = input("Enter a number (or press enter to quit): ")
    if number_input == "":
        break
    try:
        number = float(number_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid input.")
if len(numbers) == 0:
    print("No numbers were entered")
else:
    smallest = min(numbers)
    largest = max(numbers)

    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")

#4.
import random
random_number = random.randint(1, 10)
guesses = 0

while guesses < 10:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses += 1
    if guess > random_number:
        print("Your guess is too high")
    elif guess < random_number:
        print("Your guess is too low")
    else:
        print("Correct")
        break

print("Thank you for playing")


#5.
tries = 0
while tries < 5:
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_name == "JaneDoe" and password == "010203":
        print("Welcome")
        break
    else:
        print("Access denied")
        tries += 1 """


#6.
