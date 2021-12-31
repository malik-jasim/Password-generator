import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()[]{}_-"

while 1:
    password_len = int(input("The Legnth of the password you want to set: "))
    Password_count = int(input("How many passwords would you like: "))
    for x in range(0,Password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password   = password + password_char
            print("Set Your Password:", password)