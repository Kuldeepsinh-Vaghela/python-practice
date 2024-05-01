def factorial(num):
    answer = 1
    while num >=1:
        answer *= num
        num -= 1
    return answer


ans = factorial(8)
print(ans)