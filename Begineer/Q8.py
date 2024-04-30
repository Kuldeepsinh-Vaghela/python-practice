def gcd(num1,num2):
    divisor = 1
    gcd_value = 0
    while divisor <= num1 and divisor <= num2:
        if num1 % divisor == 0 and num2 % divisor == 0:
            gcd_value = divisor
            divisor += 1

        else:
            divisor += 1
    return gcd_value

def lcm(num1,num2):
    gcd_value = gcd(num1,num2)
    lcm_value = num1*num2/gcd_value

    return lcm_value


num1 = 12
num2 = 18

answer = lcm(num1,num2)
print(f"The LCM of {num1} and {num2} is",answer)