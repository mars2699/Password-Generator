# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:42 2021

@author: mars2699
"""

import random
import sys
import os
import os.path
        
print ("\nWelcome to my password generator and manager!")
userChoice = input("Press 1 to generate a password, 2 to add a new account,\nor 3 to view existing info: ")

#1) Generate a new password
if userChoice == "1":
    uppercaseLetter1 = chr(random.randint(65,90))   # Generate a random character within these ASCII ranges  
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
    
    asAList = list(passwordLinked)  # Must be a list to use shuffle
    random.shuffle(asAList)         # Randomly shuffle the order of the characters for each new password
    finalPassword = ''.join(asAList)    
    
    print('\nYour new password is: ', finalPassword)
    
#2) Create an entry for a new account and write it to a txt file
if userChoice == "2": 
        if os.path.exists("info.txt"):      # If the file already exists, "do nothing." Pass is a placeholder
            pass
        else:
            file = open("info.txt", 'w')    # Write the data file if needed
            file.close()
        file = open("info.txt", 'a')        

        accountEntry = input("Account title: ")
        usernameEntry = input("Username: ")
        passwordEntry = input("Password: ")

        userAccount = "Account Title: {}".format(accountEntry)       # Add the user's data to the text file
        userUsername = "\nUsername: {}".format(usernameEntry) 
        userPassword = "\nPassword: {}".format(passwordEntry) 
        
        file.write("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")       # Make it ~pretty!~
        file.write(userAccount)
        file.write(userUsername)
        file.write(userPassword)
        file.write("\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
        file.write("\n")
        
        print('\nYour info has been saved successfully!')
        
        file.close        
           
#3) Login to view existing info   
if userChoice == "3":
    file = open('info.txt', 'r')
    whatsInside = file.read()
    file.close()
    print(whatsInside)      # Print in the console

sys.exit()      # Close the program after each run
