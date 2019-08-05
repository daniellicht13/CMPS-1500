"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 2 Part 2
02/05/2018"""

"""This program will read user passwords, store them in a list, and convert
each password to a string of asterisks of equal length."""

#Ask user to input passwords

password = input('Please enter a password (press [enter] to finish): ')

#Store them in a list

passlist = [password]

#keep asking user for password until they enter an empty string

while password != '':
    password = input('Please enter a password (press [enter] to finish): ')
    passlist += [password]

passlist = passlist[0:-1]

#Replace passwords with string of asterisks of equal length

hiddenlist = passlist[:]

for i in range(len(hiddenlist)):
    hiddenlist[i] = int(len(hiddenlist[i]))* '*'
    
#Output the original list of passwords

print(passlist)

#Output the resuting list of asterisks

print(hiddenlist)
