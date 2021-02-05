# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:42 2021

@author: mars
"""

import random
# any other imports needed?

#A function to shuffle all the characters of the string
def shuffle(string):
  characterlist = list(string)
  random.shuffle(characterlist)
  return ''.join(characterlist)

# Add in special characters and numbers, check the average password length
# Find the right ascii codes
uppercaseLetter1=chr(random.randint(65,90)) 
# fix this lowercaseLetter2=chr(random.randint(65,90)) 
uppercaseLetter3=chr(random.randint(65,90)) 
uppercaseLetter4=chr(random.randint(65,90)) 
# make number uppercaseLetter5=chr(random.randint(65,90))
# make special character uppercaseLetter6=chr(random.randint(65,90)) 
uppercaseLetter7=chr(random.randint(65,90)) 
uppercaseLetter8=chr(random.randint(65,90))

# fix this password, sep onto new line = uppercaseLetter1 + lowercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + uppercaseLetter7 + uppercaseLetter8
password = shuffle(password)

print(password)