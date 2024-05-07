# You need to write a function that accepts an encoded string as a
# parameter.
# This string will contain a first name, last name, and an id.
# Values in the string can be separated by any number of zeros. The
# id is a numeric value but will contain no zeros. The function should
# parse the string and return a Python dictionary that contains the
# first name, last name, and id values.
# For example:
# Input : “Robert000Smith000123”
# Output:
# { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }


def decode(fnc):
    ref_fnc = fnc.replace('0',' ')
    valued_lst = ref_fnc.split(' ')
    val_lst = []
    for x in valued_lst:
        if x != '':
            val_lst.append(x)
    
    key_lst = ['first_name','last_name','id']
    dic = dict(zip(key_lst,val_lst))
    return dic

fnc = 'Robert000000000000Smith000000001237788766'
answer = decode(fnc)
print(answer)

