# Write a program to construct a dictionary from the two lists
# containing the names of students and their corresponding
# subjects. The dictionary should map the students with their
# respective subjects. Let’s see how to do this using for loops and
# dictionary comprehension.
# Input: [Sam, Alice, Mona] ,
# [Commerce, Science, Computer]
# Output: [Sam: Commerce, Alice: Science , Mona: Computer]


def dic_maker(l1,l2):
    dic = {}
    for x in range(len(l1)):
        dic[l1[x]] = l2[x]
    
    return dic

l1 = ['Sam', 'Alice', 'Mona']
l2 = ['Commerce', 'Science', 'Computer']

answer = dic_maker(l1,l2)
print(answer)




