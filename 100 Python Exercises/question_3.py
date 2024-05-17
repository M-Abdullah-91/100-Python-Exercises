# User will input (2numbers).Write a program to swap the numbers

a  = int(input("Enter First Number: "))
b = int(input("Enter second Number: "))

print(f"Before Swapping: \na={a} \nb={b}")

a = a + b  
b = a - b   
a = a - b

print(f"After Swapping: \na={a} \nb={b}")