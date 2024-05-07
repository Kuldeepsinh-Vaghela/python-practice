def Jtol():
    with open("words.txt") as file:
        txt_cont = file.read()
        ans = txt_cont.replace('j','i')
        return ans

answer = Jtol()
print(answer)



