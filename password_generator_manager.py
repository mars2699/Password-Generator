# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:42 2021

@author: Marissa Murphy
"""

import random
# import keyring

print ("Welcome to my password generator and manager!")
userChoice = input("Press 1 to generate a password, press 2 to add a new account, press 3 to remove an account, press 4 to look up an existing account, or press 5 to exit: ")

#1
def newPassword():
    uppercaseLetter1 = chr(random.randint(65,90))   
    lowercaseLetter2 = chr(random.randint(97,122)) 
    lowercaseLetter3 = chr(random.randint(97,122)) 
    lowercaseLetter4 = chr(random.randint(97,122)) 
    lowercaseLetter5 = chr(random.randint(97,122))
    lowercaseLetter6 = chr(random.randint(97,122))
    lowercaseLetter7 = chr(random.randint(97,122))
    lowercaseLetter8 = chr(random.randint(97,122))
    lowercaseLetter9 = chr(random.randint(97,122))
    lowercaseLetter10 = chr(random.randint(97,122))
    number11 = chr(random.randint(48,57))
    specCharacter = chr(random.randint(33,38))

    passwordLinked = uppercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + lowercaseLetter5 + lowercaseLetter6 + lowercaseLetter7 + lowercaseLetter8 + lowercaseLetter9 + lowercaseLetter10 + number11 + specCharacter
    finalPassword = random.shuffle(passwordLinked)    
    print('Your new password is: ',finalPassword)

#2    
def addAccount():
    account = input("Account Title: ")
    username = input("Username: ")
    password = input("Password: ")

#3
def delAccount():
    deleteChoice = input("What account do you want to delete?: ")

#4
def search():
    wantedAccount = input("Which account are you looking for?: ")
    #get_keyring()

#5
def bye():
    print("Bye for now!")
    exit()

if userChoice == "1":
    newPassword()

