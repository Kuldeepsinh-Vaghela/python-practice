# Write a Python program to find if a given string starts with a
# given character using Lambda.
# Sample input: input_string = "Hello, World!", given_char = "H"
# Sample Output: True


def string_checker(inp_str,given_char):
    answer  = lambda x: True if inp_str[0] == x else False
    print(answer(given_char))

inp_str = "Hello World!"
given_char = "H"


answer = string_checker(inp_str,given_char)
