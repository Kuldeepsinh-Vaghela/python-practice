def anagram_check(string1, string2):
    for alpha in string1:
        if alpha not in string2:
            return "No"
    return "Yes"

string1 = "cider"
string2 = "cried"

answer = anagram_check(string1,string2)
print(f"Is '{string1}' anagram of '{string2}?'",answer)
    


