
def find_even_len_str():
    with open("doc.txt") as file:
        str_value = file.read()
    list_str = str_value.split(" ")
    answer = []
    for str in list_str:
        if len(str) % 2 == 0:
            answer.append(str)
    return answer
    

answer = find_even_len_str()
print(answer)
    
