def q1(number):
    if number%3 == 0:
        if number % 5 == 0:
            print("Consultadd-Python Training")
        else:
            print("Consultadd")
    elif number%5 == 0:
        if number % 3 == 0:
            print("Consultadd-Python Training")
        else:
            print("Python Training")
    else:
        print("The nuber is not divisible by 3 or 5")


a = q1(7)

