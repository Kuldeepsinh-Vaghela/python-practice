# Given an input string, write a function that returns the run
# length encoded string for the input string.
# For Example:
# Input: wwwwaaadebbbbbw
# Output: w4a3d1e1b5w1

def encoder(fnc):
    value = ''
    count = 0
    answer = ''
    for x in range(len(fnc)):
        if fnc[x] != value:
            if x != 0:
                answer += value
                answer += str(count)
                value = fnc[x]
                count = 0
                count += 1
            else:
                value = fnc[x]
                count = 0
                count += 1
        else:
            count += 1
        
        if x == len(fnc)-1:
            answer += value
            answer += str(count)
    return answer


ans = encoder('wwwwaaadebbbbbwwwrtyyytrr')
print(ans)
        

