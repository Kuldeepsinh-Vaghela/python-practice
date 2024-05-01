def perfect_num_check(num):
    divisor = 1
    sum_value = 0
    while divisor < num:
        if num % divisor == 0:
            sum_value += divisor
            divisor += 1
        else:
            divisor += 1
    if sum_value == num:
        return "Yes"
    else:
        return "No"

number = 4
answer = perfect_num_check(number)
print(f"Is {number} a perfect number?",answer)
