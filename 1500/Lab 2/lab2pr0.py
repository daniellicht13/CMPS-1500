"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 2 Part 0
02/05/2018"""

"""This program ask a user to input a line of text, and outputs
a secure password consisiting the first character of each word
and punctuation. The program also changes the characters 'A',
'L', 'O' to '@', '1', '0' respectively."""

#asks user to enter a phrase

password = (input('Please enter a phrase: '))

#Adds first charcter to password 

if password[0] == 'a': 
     newpassword = '@'
elif password[0] == 'l': 
     newpassword = '1'
elif password[0] == 'o':
     newpassword = '0'
else:
     newpassword = (password[0])

#converts the first charcter of each word into a symbol if necessary and then adds new charcter to the new password 

punc = '.,?!:;'

for i in range(len(password)):
     if password[i] == ' ':      
          if password[i+1] == 'a':
               newpassword = newpassword + '@'
          elif password[i+1] == 'l':
               newpassword = newpassword + '1'
          elif password[i+1] == 'o':
               newpassword = newpassword + '0'
          else:
               newpassword = newpassword + (password [i+1])
     elif password[i] in punc:       #includes punctuation into new password
          newpassword = newpassword + (password [i])


#outputs newly generated password
          
print(newpassword)

