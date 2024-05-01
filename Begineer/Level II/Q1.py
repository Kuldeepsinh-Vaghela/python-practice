# Write a Python program to find the common elements between two lists.
# Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
# Sample output: [4, 5]

def common_ele_finder(l1,l2):
    answer = []
    for value in l1:
        if value in l2:
            answer.append(value)
    return answer


l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]

ans = common_ele_finder(l1,l2)
print(ans)

