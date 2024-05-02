# Write a Python function that counts the number of vowels in a
# given string.
# Sample Input: string = "Hello, World!"
# Sample Output: Number of vowels: 3

def vowels_counter(str_value):
    vowels = 'aeiou'
    answer = 0
    for x in str_value:
        if x in vowels:
            answer += 1
    return answer

str_value = 'Hello, World!'

answer = vowels_counter(str_value)
print(answer)