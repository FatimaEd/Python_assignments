
""""#1.
import random
def dice_roll():
    return random.randint(1,6)

def main():
    roll_count = 0
    result = 0

    while result != 6:
        result = dice_roll()
        roll_count += 1
        print(f"You rolled a {result}")
main()

#2.
import random
def dice_roll(max_number):
    return random.randint(1, max_number)

def main():
    max_number = int(input("Enter the maximum numer of the dice: "))
    roll_count = 0
    result = 0

    while result != max_number:
        result = dice_roll(max_number)
        roll_count += 1
        print(f"You rolled a {result}")
main()"""

#3.
