# Write a Python program to reverse a number using a while
# loop.
# Sample Input: num = 12345
# Sample Output: revnum = 54321

def reverse(num):
    str_num = str(num)
    counter = len(str_num)-1
    answer_str = ''
    while counter >= 0:
        answer_str += str_num[counter]
        counter -= 1
    return int(answer_str)


answer = reverse(12345)
print(answer)

