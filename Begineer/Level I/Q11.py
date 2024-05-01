# Write a Python program to calculate the sum of digits of a given
# number until the sum becomes a single-digit number.
# Sample Input: num = 987
# Sample Output: Sum_of_digits = 24,
# Again compute the sum of digits so that it can be reduced to
# on single digit.
# Final Output: 6


def sum_compute(num):
    str_num = str(num)
    count = 0
    for x in str_num:
        value = int(x)
        count += value
    return count

def sum_digits(num):
    new_num = str(num)
    new_lst = list(new_num)
    while len(new_lst) != 1:
        int_num = int(new_num)
        new_num = sum_compute(int_num)
        new_num = str(new_num)
        new_lst = list(new_num)
    return int(new_num)

answer = sum_digits(441)
print(answer)

