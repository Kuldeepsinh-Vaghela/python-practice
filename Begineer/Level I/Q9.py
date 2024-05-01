# Write a Python program to count the frequency of each element
# in a list.
# Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5] 1,1,2,2,2,3,4,4,5
# Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}


def freq_counter(inp_list):
    sorted_list = sorted(inp_list)
    counter = 0
    list_counter = 0
    value = 0
    frequency_count = {}
    
    while list_counter < len(sorted_list):
        if value == 0:
            value = sorted_list[list_counter]
            counter += 1
            list_counter += 1
        elif value == sorted_list[list_counter]:
            counter += 1
            list_counter += 1
        else:
            frequency_count[value] = counter
            value = 0
            counter = 0
    
    if value != 0:
        frequency_count[value] = counter
    
    return frequency_count

            

a = freq_counter([1, 2, 3, 2, 4, 1, 2, 4, 5])
print(a)




        
        
        
        


