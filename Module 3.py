#1.
zander_length = int(input("Enter the fish length: "))
if zander_length < 42:
    print("Release the fish back into the lake")
    print(f"You are {42 - zander_length}cm below the size limit.")

#2.

cabin_class = input("Enter the cabin class: ")
if cabin_class == "LUX" or "lux":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A" or "a":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B" or "b":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C" or "c":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

#3.
value = float(input("Enter the hemoglobin value (g/l): "))
gender = input("Enter your gender (Male/Female): ")


if gender == "Female" or gender == "female":
    if 117 <= value <= 155:
        print("you have a normal hemoglobin value")
    elif value < 117 :
        print("you have a low hemoglobin value")
    else:
        print("you have a high hemoglobin value")

elif gender == "Male" or gender == "male":
    if 134 <= value <= 167:
        print("you have a normal hemoglobin value")
    elif value < 134:
        print("you have a low hemoglobin value")
    else:
        print("you have a high hemoglobin value")

#4.
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("This is a leap year")
elif year % 100 != 0 or (year % 100 == 0 and year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")






