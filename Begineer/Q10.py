# Write a Python program to reverse the order of words in a given
# sentence.
# Input_sentence = “Hello, World! Welcome to Python
# programming.”
# Output after reverse = “programming. Python to Welcome
# World! Hello,”

def reverse_order(inp_str):
    lst_str = inp_str.split(" ")
    new_lst = lst_str[::-1]
    new_str = " ".join(new_lst)
    return new_str





inp_str = "Hello, World! Welcome to Python programming."
answer = reverse_order(inp_str)

print(answer)