# Write a Python program that executes an operation on a list and
# handles an IndexError exception if the index is out of range.


def list_iter(lst):
    counter = 0
    while counter < 6:
        try:
            print(lst[counter])
            counter += 1
        except IndexError:
            print("The list is completed")
            counter += 1



answer = list_iter([1,2,3,4])


