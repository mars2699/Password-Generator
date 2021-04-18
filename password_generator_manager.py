# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:42 2021

@author: Marissa Murphy
"""

import random
import csv
#from cryptography.fernet import Fernet

print ("Welcome to my password generator and manager!")
userChoice = input("Press 1 to generate a password, 2 to add a new account, 3 to view existing info, or 4 to exit: ")

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
def addAccount():
    with open('my_account_list.csv', 'a') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL) 
        #while (1):
        account = input("Account Title: ")
        username = input("Username: ")
        password = input("Password: ")
        w.writerow([account, username, password])
        print('\nYour info has been saved successfully!')
        # encrypt file here

#3) View an existing account so the user can see their info
#def search():
    # decrypt file here
    #wantedAccount = input("Which account are you looking for?: ")

#4) Exit
#def bye():
   # print("Bye for now!")
   # exit()
    
########################################################################   

if userChoice == "1":
    newPassword()
if userChoice == "2":
    addAccount()
