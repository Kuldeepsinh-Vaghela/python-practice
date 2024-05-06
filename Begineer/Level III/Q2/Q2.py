#  Write a program to count the lines in a file “demo.txt”


def line_counter(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            lines_count = len(lines)
            print(f"File '{file_name}' has {lines_count} lines.")
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.")



line_counter('demo.txt')