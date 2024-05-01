def grade_finder(percentage):
    if percentage >= 90:
        return "Grade A"
    elif percentage >= 80:
        return "Grade B"
    elif percentage >= 70:
        return "Grade C"
    elif percentage >= 60:
        return "Grade D"
    elif percentage >= 40:
        return "Grade E"
    else:
        return "Grade F"
    

def result(physics,chemistry,biology,mathematics,computer):
    print("Physics:",grade_finder(physics))
    print("chemistry:",grade_finder(chemistry))
    print("biology:",grade_finder(biology))
    print("mathematics:",grade_finder(mathematics))
    print("computer:",grade_finder(computer))


physics = int(input("Please enter your score in Physics"))
chemistry = int(input("Please enter your score in Chemistry"))
biology = int(input("Please enter your score in Biology"))
mathematics = int(input("Please enter your score in Mathematics"))
computer = int(input("Please enter your score in Computer"))

result(physics,chemistry,biology,mathematics,computer)
    
