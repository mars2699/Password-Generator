# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:42 2021

@author: mars2699
"""

import random
import csv
from cryptography.fernet import Fernet

print ("Welcome to my password generator and manager!")
userChoice = input("Press 1 to generate a password, 2 to add a new account, or 3 to view existing info: ")

#1) Generate a new password
def newPassword():
    uppercaseLetter1 = chr(random.randint(65,90))   
    lowercaseLetter2 = chr(random.randint(97,122)) 
    lowercaseLetter3 = chr(random.randint(97,122)) 
    lowercaseLetter4 = chr(random.randint(97,122)) 
    uppercaseLetter5 = chr(random.randint(65,90))
    lowercaseLetter6 = chr(random.randint(97,122))
    lowercaseLetter7 = chr(random.randint(97,122))
    lowercaseLetter8 = chr(random.randint(97,122))
    lowercaseLetter9 = chr(random.randint(97,122))
    lowercaseLetter10 = chr(random.randint(97,122))
    number11 = chr(random.randint(48,57))
    specCharacter = chr(random.randint(33,38))

    passwordLinked = uppercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + uppercaseLetter5 + lowercaseLetter6 + lowercaseLetter7 + lowercaseLetter8 + lowercaseLetter9 + lowercaseLetter10 + number11 + specCharacter   
    print('Your new password is: ',passwordLinked)
    
#2) Create an entry for a new account and write it to a csv file
def makeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def loadKey():
    return open("key.key", "rb").read()

def addAccount():
    with open('my_account_list.csv', 'a') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL) 
        #while (1):
        account = input("Account Title: ")
        username = input("Username: ")
        password = input("Password: ")
        w.writerow([account, username, password])
        print('\nYour info has been saved successfully!')
        
        makeKey()
        key = loadKey()
        username.encode()
        password.encode()
        f = Fernet(key)
        encryptedUsername = f.encrypt(username)
        encryptedPassword = f.encrypt(password)
        print(encryptedUsername)
        print(encryptedPassword)

#3) View an existing account so the user can see their info
def search():
    decrypted_encrypted1 = f.decrypt(encryptedUsername)
    decrypted_encrypted2 = f.decrypt(encryptedPassword)
    print(decrypted_encrypted1)
    print(decrypted_encrypted2)
    #wantedAccount = input("Which account are you looking for?: ")
    
########################################################################   

if userChoice == "1":
    newPassword()
if userChoice == "2":
    loadKey()
    addAccount()
if userChoice == "3":
    search()
else:
    print('Invalid input. Please enter a number from 1-3 followed by the enter key.')
