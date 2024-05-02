# Given an array of size N. The task is to rotate array by D elements
# towards right
# Sample Input: arr = [1, 2, 3, 4, 5], D = 2
# Sample Output: arr after rotation = [4, 5, 1, 2, 3]


def rotate_arr(arr,trgt):
    if len(arr) != 0:
        lst_counter = len(arr)-1
        counter2 = 0
        while trgt > 0:
            last_ele = arr[lst_counter]
            del arr[lst_counter]
            arr.insert(counter2,last_ele)
            trgt -= 1
    else:
        return arr
    return arr


answer = rotate_arr([1,2,3,4,5], 2)
print(answer)


