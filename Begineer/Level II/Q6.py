# Write a Python program to check if a number is a power of two
# using recursion.



def check_two_power(num):
    if num == 1:
        print("Yes")
    elif num <= 0 or num % 2 != 0:
        print("No")
    else:
        check_two_power(num // 2)


answer = check_two_power(31)
