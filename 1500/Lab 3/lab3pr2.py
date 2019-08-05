"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 3 Part 2
02/16/2018"""

'''This program asks a user to input a file with a list of widths and lengths
of rooms in a floor of a house. The program then calculates the area of the
given rooms, sums them up, and outputs the total area of the floor.'''

#Ask user to enter file name

filename = input('Please enter file name: ')

#Read area file and turn it into a list

f = open(filename, 'r')
text = f.read()
f.close()
wordlist= text.split()

#Convert list into integers

for i in range(len(wordlist)):
    wordlist[i] = int(wordlist[i])
       
'''
    Calculates the area of a room
    Args:
        w (int): Width of room
        h (int): Length of room
    Returns:
        int: Area of given room
'''

def area(w,h):
    return (w * h)

#Assign first number of each pair to width and second number to length
#Add area of each room to total house area

house = 0
for i in range(0,len(wordlist),2):
    room = area(wordlist[i],wordlist[i+1])
    house += room

#Print total area
    
print('The calculated area is:',house)
        

