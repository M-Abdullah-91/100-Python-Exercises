# User will input (3ages).Find the oldest one

age1 = int(input("Enter Age 1: "))
age2 = int(input("Enter Age 2: "))
age3 = int(input("Enter Age 3: "))

if age1 > age2 and age1 > age3:
    print("Age 1 is Greater")
elif age2 > age3:
    print("Age 2 is Greater")
else:
    print("Age 3 is Greater")

