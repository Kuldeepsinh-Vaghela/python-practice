# Write a Python program to create a list of given strings
# individually of the list using the Python map function.
# Eg. Input:
# ['Red', 'Blue', 'Black', 'White', 'Pink']
# Output:
# [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i',
# 'n', 'k']]


def lst_of_string(str_value):
    opt = list(str_value)
    return opt

lst = ['Red', 'Blue', 'Black', 'White', 'Pink']
answer = map(lst_of_string,lst)
print(list(answer))

