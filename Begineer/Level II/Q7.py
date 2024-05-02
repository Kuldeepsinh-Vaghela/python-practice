# Write a Python function that finds the median of a list of
# numbers.
# Sample Input: number_list = [7, 2, 5, 1, 9, 3]
# Sample Output: Median: 4.0



def median_finder(lst):
    sorted_lst = sorted(lst)
    len_lst = len(sorted_lst)
    if len_lst % 2 == 0:
        num1 = sorted_lst[int(((len_lst)/2)-1)]
        num2 = sorted_lst[int(((len_lst)/2))]
        median = (num1 + num2) / 2
        return median
    else:
        median = sorted_lst[int(((len_lst+1)/2)-1)]
        return median
    


answer = median_finder([7, 2, 5, 1, 9, 3])
print(answer)

