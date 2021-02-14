# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:05:42 2021

@author: mars2699
"""

import random

# Def function marks a new function call. Our password is one big string.
def shuffle(string):    
  characterList = list(string)  # Store all pieces into single variable.
  random.shuffle(characterList)
  return ''.join(characterList) # End of function call, joins all elements 
# I learned while making this code to use ''. for unseparated list elements. 
# We are printing a password rather than sentences.

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
password = shuffle(password)    # We want a unique password every time

print('Your new password is: ',password)
