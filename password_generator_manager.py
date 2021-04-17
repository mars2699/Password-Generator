# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:42 2021

@author: Marissa Murphy
"""

import random
import csv
from cryptography.fernet import Fernet

print ("Welcome to my password generator and manager!")
userChoice = input("Press 1 to generate a password, press 2 to add a new account, press 3 to remove an account, press 4 to look up an existing account, or press 5 to exit: ")

#1) Generate a new password
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
    print('Your new password is: ',passwordLinked)
    
#2) Create an entry for a new account and write it to a csv file
#def addAccount():
    #with open('my_account_list.csv', 'a') as f:
        #w = csv.writer(f, quoting=csv.QUOTE_ALL) 
    #while (1):
        #account = input("Account Title: ")
        #username = input("Username: ")
        #password = input("Password: ")
        #w.writerow([account, username, password])
    
# Encrypt this csv file
# Use fernet to encrypt the user's data in a file. First generate a key.
#key = Fernet.generate_key()
  
# Create a key to decrypt the data with. The file is called 'uniquekey.key'
#with open('uniquekey.key', 'wb') as filekey:
   #filekey.write(key)
   
# Open the key
#with open('uniquekey.key', 'rb') as filekey:
    #key = filekey.read()
  
# Use the key
#fernet = Fernet(key)
  
# Open the original file you want to encrypt
#with open('my_account_list.csv', 'rb') as file:
    #original = file.read()
      
# Encrypt the file
#encrypted = fernet.encrypt(original)
  
# Open the csv file in write mode and write in the data you want to encrypt
#with open('my_account_list.csv', 'wb') as encrypted_file:
   # encrypted_file.write(encrypted)

#3) Delete an existing account
#def delAccount():
    #deleteChoice = input("What account do you want to delete?: ")

#4) Search for an existing account so the user can see their info
#def search():
    #wantedAccount = input("Which account are you looking for?: ")

#5) Exit
#def bye():
    #print("Bye for now!")
    #exit()
 
    
 
    
########################################################################

    
# using the key
#fernet = Fernet(key)
  
# opening the encrypted file
#with open('my_account_list.csv', 'rb') as enc_file:
    #encrypted = enc_file.read()
  
# decrypting the file
#decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and writing the decrypted data
#with open('my_account_list.csv', 'wb') as dec_file:
    #dec_file.write(decrypted)

if userChoice == "1":
    newPassword()
