from curses.ascii import (islower,  isupper)

valid1 = False
valid2 = False
valid3 = False
valid4 = False
valid5 = False
test = 5
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special=['!','@','#','$','%','^','&','*','(',')','-','_','+','=','']

print("Password strength checker")

password = input("Enter your password: ")

file = open("100k-most-used-passwords-NCSC.txt", "r")

if password in file.read():
    valid1 = True

list = list(password)

for sign in list:
    if sign.isupper():
        valid2 =True

for sign in list:
    if sign.islower():
        valid3 = True

for sign in list:
    if sign in numbers:
        valid4 = True

for sign in list:
    if sign in special:
        valid5 = True

if valid1 == True:
    print("Your password is among the 100k most used passwords, please change it.")
    test -= 1 
if valid2 == False:
    print("Your password does not contain an uppercase letter, please change it.")
    test -= 1   
if valid3 == False:
    print("Your password does not contain a lowercase letter, please change it.")
    test -= 1
if valid4 == False:
    print("Your password does not contain a number, please change it.")
    test -= 1
if valid5 == False:
    print("Your password does not contain a special character, please change it.")
    test -= 1

print("Rating: ", test, "/5")