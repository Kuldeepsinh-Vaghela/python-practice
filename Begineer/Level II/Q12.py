# Create a login page backend to ask users to enter the username
# and password. Make sure to ask for a Re-Type Password and if the
# password is incorrect give a chance to enter it again but it should
# not be more than 3 times.


storage = {}
password_reset_count = 3

def credential_matching(username, password):
    global storage
    if username in storage:
        if password == storage[username]:
            return True
        else:
            return False
    


def login_page():
    global storage
    global password_reset_count
    r_l = input("Please type 'r' for register or 'l' for login\n")
    if r_l == 'r':
        username_inp = input("Please enter the username\n")
        password_inp = input("Please enter the password\n")
        retype_password = input("Please retype your password\n")
        while password_inp != retype_password:
            print("The passwords don't match! Please type again")
            retype_password = input("Please retype your password\n")
            
        storage[username_inp] = password_inp
        login_page()
    else:
        username_inp = input("Please enter the username\n")
        password_inp = input("Please enter the password\n")
        match = credential_matching(username_inp,password_inp)
        if match:
            print(f"Your username is {username_inp} and password is {password_inp}")
        elif username_inp not in storage:
            print("The username entered is not registered. Please register first")
            return login_page()
        else:
            while match == False and password_reset_count > 0:
                password_reset_count -= 1
                print(f"The password entered is incorrect! You have {password_reset_count} remaining ")
                password_new = input("Please enter the password")
                match = credential_matching(username_inp,password_new)
                continue
            if storage [username_inp] != password_inp:
                print("Too many attempts for login! Try again later")
            else:
                print(f"Your username is {username_inp} and password is {password_inp}")


if __name__ == "__main__":
    login_page()







