import os
from cryptography.fernet import Fernet


# Checks for 'info file' which contains encrypted username and password
# if the file exists, it continues else creates the file and closes the file
# as the fil is newly created it does not have any registered account hence calls signup function
def file_check():
    if os.path.isfile("./acc_details.txt") == True:
        preference_check()
    else:
        acc_file = open("acc_details.txt", "w")
        acc_file.close()
        signup()


# Preference_check prompts the user to either login or signup and then calls the required function
def preference_check():
    print("Enter LOGIN to login or SIGNUP to create a new account")
    response = custom_input()
    if response == "login":
        login()
    elif response ==  "signup":
        signup()
    else:
        preference_check()


# This is the main funtion for logging in
# First it clears the screen, opens the 'info file' and takes in the username and pssword as input
def login():
    clr_scrn()
    print("LOGIN")
    acc_file = open("acc_details.txt", "r")
    usrname = input("Enter your Username: ")
    passwrd = input("Enter your password: ")
    
    # This is the decryptor and verifier
    # It reads each line in the file, stores the encrypted hash in the variable 'enc_hash' and removes the newline character
    # The encrypted hash has two parts - the key required for decryption and the encrypted message itself
    # This encrypted hash is split into these parts and stored in a list
    # 'f' is Fernet object that holds the key for encryption and decryption and the key is given to it
    # In the if statement, the key is first decrypted and then decoded and the return type of 'decrypt()' is byte
    # Then it is checked with the enterd username and password and does the required action
    for line in acc_file:
        enc_hash = line.strip("\n")
        keynhash = enc_hash.split()

        f = Fernet(keynhash[0])
        if f.decrypt(keynhash[1]).decode() == usrname + passwrd:
            print("Successful")
            break
    else:
        print("Unsuccessful. No such account found.")
    acc_file.close()

# This is the main function for signing  up
# First it clears the screen, opens the 'info file' and takes in the username and pssword as input
def signup():
    clr_scrn()
    print("SIGNUP")
    acc_file = open("acc_details.txt", "a")
    usrname = input("Enter your Username: ")
    passwrd = input("Enter your password: ")

    # This is the encrypter
    # It generates a key, store it and passes the key to 'f' which is a Fernet object (Fernet objects need a key to encrypt and decrypt)
    # Then 'enc_hash' takes the key, adds a whitespace for separation and encrypts both the username and password together
    # Username and password are encoded as fernet uses 'bytes' instead of 'strings'
    # 'enc_hash' is written to the 'info file' with a newline character to make each account distinguishable
    key = Fernet.generate_key()
    f = Fernet(key)
    enc_hash = key + b" " + f.encrypt(usrname.encode() + passwrd.encode())

    acc_file.write(enc_hash.decode() + "\n") 
    acc_file.close()


# Custom input is used only in 'preference_check()'
# It is to make sure any blank space is removed and all the characters are in lower case for easier matching with if statement
def custom_input():
    usr_input = input()
    usr_input = usr_input.lower()
    usr_input = usr_input.replace(" ", "")
    return usr_input


# This is a function to clear the screen to give the user a feel of navigating to a new page
def clr_scrn():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Safety check to prevent the program from executing when called as a module in another file
if __name__ == "__main__":
    file_check()

# To make sure the program dosen't close immediately after execution
input() 