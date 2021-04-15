# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:42 2021

@author: Marissa Murphy
"""

import random


print ("Welcome to my password generator and manager!")
userChoice = input("Press 1 to generate a password, press 2 to add a new account, press 3 to remove an account, press 4 to look up an existing account, or press 5 to exit: ")

def newPassword():
# Randint randomizes between given range only
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

    password = uppercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + \
            lowercaseLetter4 + lowercaseLetter5 + lowercaseLetter6 + \
            lowercaseLetter7 + lowercaseLetter8 + lowercaseLetter9 + \
            lowercaseLetter10 + number11 + specCharacter
    password = shuffle(password)    
print('Your new password is: ',password)
    
def addAccount():
    account = input("Account Title: ")
    username = input("Username: ")
    password = input("Password: ")

def delAccount():

def search():

def bye():

