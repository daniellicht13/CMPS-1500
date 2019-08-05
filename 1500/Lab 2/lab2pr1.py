"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 2 Part 1
02/05/2018"""

""" This program asks a user to enter a password. The program does not accept
the password unless its length is between 8 and 20 characters, it doesn't
contain spaces, and it contains at least one uppercase letter, one lowercase
letter, a symbol, and a number."""

password = input('Please enter a password:\n')

symbols = '!?,.;:$#_&'            
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
space = ' '

#Set all variables neccessary for proper password to False

newpassword = False       
length = False 
upper = False
lower = False
num = False
sym = False
spc= True 

#Test for all variables. If at least one is false, asks user for new password.

while newpassword == False: 
    for i in password:                                  
        if len(password) > 7 and len(password) < 21:    
            length = True                               
        if i in uppercase:
            upper = True
        if i in lowercase:
            lower = True
        if i in number:
            num = True
        if i in symbols:
            sym = True
        if i in space:
            spc = False
        if length == True and upper == True and lower == True and num == True and sym == True and spc == True:  
            newpassword = True
    if newpassword == False:                      #reset all variables to original boolean value before looping again
        password = input('Please enter a password:\n')
        length = False 
        upper = False
        lower = False
        num = False
        sym = False
        spc= True 

#Prints password accepted
        
if newpassword == True:
    print('Password accepted')
        




