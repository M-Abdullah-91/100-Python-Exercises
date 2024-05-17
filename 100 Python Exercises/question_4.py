# Write a program that will give you the sum of 3 digits

num = int(input("Enter 3 digits: "))

# sum = 0

# for i in a:
#     sum += int(i)
    
    
# print(f"Sum of {a} is {sum}")

# suppose number is 345
a = num % 10    #  (345%10) = 5
num  = num  // 10   #  (345 // 10 ) = 34
b = num % 10    # (345 % 10 ) = 4
c = num // 10     # 3


sum = a + b + c

print(f"Sum is {sum}")