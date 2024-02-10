import os

#Referred W3Schools
def file_check():
    if os.path.isfile("./acc_details.txt") == True:
        pref_check()
    else:
        acc_file = open("acc_details.txt", "w")
        acc_file.close()
        signup()


def pref_check():
    print("Enter LOGIN to login or SIGNUP to create a new account")
    response = custom_input()
    if response == "login":
        login()
    elif response ==  "signup":
        signup()
    else:
        pref_check()

def login():
    clr_scrn()
    print("LOGIN")
    acc_file = open("acc_details.txt", "r")
    usrname = input("Enter your Username: ")
    passwrd = input("Enter your password: ")
    usr_check = usrname + passwrd + "\n"
    
    for line in acc_file:
        if line == usr_check:
            print("Success")
            break
    else:
        print("Unsuccessful")
    acc_file.close()

def signup():
    clr_scrn()
    print("SIGNUP")
    acc_file = open("acc_details.txt", "a")
    usrname = input("Enter your Username: ")
    passwrd = input("Enter your password: ")
    acc_file.write(usrname + passwrd + "\n") 
    acc_file.close()


def custom_input():
    usr_input = input()
    usr_input = usr_input.lower()
    usr_input = usr_input.replace(" ", "")
    return usr_input


#Referred W3Schools
def clr_scrn():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    file_check()

input()