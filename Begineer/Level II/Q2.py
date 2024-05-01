# Create a function that takes a list and returns a new list with unique elements 
# of the first list.
# Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5] Sample Output: list2 = [1, 2, 3, 4, 5]

def uniq_elements_finder(l1):
    ans_list = []
    for x in l1:
        if x not in ans_list:
            ans_list.append(x)
    return ans_list


l1 = [1,2,2,3,4,4,5,5,6,6,6,6,7,7,8,9,10]

answer = uniq_elements_finder(l1)
print(answer)
