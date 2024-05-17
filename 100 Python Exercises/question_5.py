# Write a program that will reverse a four digit number.Also it checks
# # whether the reverse is true.


num = int(input("Enter a 5 digit number: ")) # 1234


user_input = num

a = num % 10    # 4
num = num // 10     # 123
b = num % 10    # 3
num = num // 10     # 12
c = num % 10    # 2
num = num // 10
d = num % 10   # 1
e = num // 10

# print(10000*a)
# print(1000*b)
# print(100*c)
# print(10*d)
# print(e)


rev_num = 10000 *a + 1000*b + 100*c + 10*d + e

print(f"Reverse string is {rev_num}")

if user_input == rev_num:
    print("Equal")
else:
    print("Not Equal")