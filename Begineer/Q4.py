def find_odd(start,stop):
    sum_odd_num = 0
    while start <= stop:
        if start % 2 != 0 :
            sum_odd_num += start
            start += 1
        else:
            start += 1
    return sum_odd_num


answer = find_odd(1,100)
print(answer)




