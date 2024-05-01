inp_string = input("Please enter the string\n")
def counter(inp_string):
    alphabets = 0
    numbers = 0
    for x in inp_string:
        if x.isalpha():
            alphabets += 1
        elif x.isnumeric():
            numbers += 1
        
    print("Alphabets:",alphabets, "&","Number:",numbers)

counter(inp_string)