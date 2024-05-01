# Given an array of N integers and an integer K, find the number of pairs of elements 
# in the array whose sum is equal to K.
# Sample Input: arr = [1, 2, 3, 4, 5], k = 6
# Sample Output: Pair count: 2


def find_sum(lst,trgt):
    pairs = 0
    for x in lst:
        indx = lst.index(x)
        rem_val = trgt - x
        if rem_val in lst[indx+1:]:
            pairs += 1
    return pairs

lst = [-1, 0, 1]
trgt = 0

answer = find_sum(lst,trgt)
print(answer)