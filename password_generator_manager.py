# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:42 2021

@author: mars2699
"""

import random
import csv
import sys
from cryptography.fernet import Fernet
#from make_key import *

# Please download make_key.py and my_account_list.csv before running

print ("\nWelcome to my password generator and manager!")
userChoice = input("Press 1 to generate a password, 2 to add a new account,\nor 3 to view existing info: ")

#1) Generate a new password
if userChoice == "1":
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

    passwordLinked = (uppercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + 
                      uppercaseLetter5 + lowercaseLetter6 + lowercaseLetter7 + lowercaseLetter8 + 
                      lowercaseLetter9 + lowercaseLetter10 + number11 + specCharacter) 
    
    asAList = list(passwordLinked)
    random.shuffle(asAList)
    finalPassword = ''.join(asAList)
    
    print('\nYour new password is: ', finalPassword)
    
#2) Create an entry for a new account and write it to a csv file
if userChoice == "2":
    with open('my_account_list.csv', 'a') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL) 
        account = input("Account Title: ")
        username = input("Username: ")
        password = input("Password: ")
        w.writerow([account, username, password])
        print('\nYour info has been saved successfully!') 
        
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encPassword = fernet.encrypt(password.encode())
        print("original string: ", password)
        print("encrypted string: ", encPassword)
        
#3) View existing info 
if userChoice == "3":
    decPassword = fernet.decrypt(encPassword).decode()
    
    with open('my_account_list.csv', newline='') as csvfile:
        infoReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in infoReader:
            print(', '.join(row))

sys.exit()
