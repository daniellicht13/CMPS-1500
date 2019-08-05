# Lab problem: "Lights On!"
#
"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 7 Part 0
04/06/2018"""



# Most of your Lab code will go here:

import time    #provides time.sleep(0.5)
from random import *    #provides choice([0,1]), etc.
import sys    #larger recursive stack
sys.setrecursionlimit(100000)   #100,000 deep - in theory

def runGenerations(aList, x = 0):
    """ runGenerations keeps running the evolve function...
    """
    print(aList)    #display the list, aList
    newList = evolve(aList)
    if isAllOnes(newList) == True:
        print(newList)
        return x + 1
    else:
        runGenerations(newList, x + 1) #recur

"""Statistically, the expected number of steps is 1 / (0.5^n), n being
the number of elements in the list. So a 5-element list would be expected
to take 1 / (0.5^5) = 1 / 0.03125 = 32 steps.
"""
def evolve(aList):
    """ evolve takes in a list of integers, aList,
        and returns a new list of integers
        considered to be the "next generation"
    """
    n = len(aList)  #n now holds the length of the list aList
    newList = [setNewElement(aList, i) for i in range(n)]
    return newList
def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
        input aList: any list of integers
        input i: the index of the new element to return
        input x: an extra, optional input for future use
    """
    # this returns the ith element of the new list! That is, newList[i]
    return aList[i] + 1

""" runGenerations calls evolve which calls setNewElement which increments
each integer element in a list by 1. The list with the incremented values
is returned as newList in the evolve function. Finally, runGenerations
keeps the evolve function running and prints the incremented lists with
each recursion.
"""

#Question 0
def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
        input aList: any list of integers
        input i: the index of the new element to return
        input x: an extra, optional input for future use
    """
    return aList[i] * 2

#Question 1
def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
        input aList: any list of integers
        input i: the index of the new element to return
        input x: an extra, optional input for future use
    """
    return aList[i] ** 2

#Question 2
def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
        input aList: any list of integers
        input i: the index of the new element to return
        input x: an extra, optional input for future use
    """
    return aList[i - 1]

#Question 3
def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
        input aList: any list of integers
        input i: the index of the new element to return
        input x: an extra, optional input for future use
    """
    if i < (len(aList) - 1):
        return aList[i + 1]
    else:
        return aList[0]

#Question 4
def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
        input aList: any list of integers
        input i: the index of the new element to return
        input x: an extra, optional input for future use
    """
    aList[i] = choice([0, 1])
    if i == (len(aList) - 1):
        return aList[i]
    else:
        return setNewElement(aList, i + 1)
        
def isAllOnes(aList):
    """ Tests whether all elements in list are the integer 1
        Args:
            aList (list): List of integers
        Returns:
            bool: True if all 1s or False if not
    """
    x = (len(aList) - 1)
    if x == -1:
        return True
    if aList[x] == 1:
        return isAllOnes(aList[0:-1])
    else:
        return False
 
       
def evolve(aList):
    """evolve takes in a list of integers, aList,
        and returns a new list of integers
        considered to be the "next generation"
    """
    n = len(aList)    #n now holds the size of the list aList
    x = int(input("Enter an index to change: "))    #Get numeric input from user
    return [setNewElement(aList, i, x) for i in range(n)]

def setNewElement(aList, i, x = 0):
    """setNewElement returns the NEW list's ith element
        input aList: any list of integers
        input i: the index of the new element to return
        input x: the user's chosen column
    """
    if i == x - 1:    #if it's the user's chosen column,
        return abs(aList[i] - 1)
    elif i == x:
        return abs(aList[i] - 1)
    elif i == x + 1:
        return abs(aList[i] - 1)
    else:    #otherwise,
        return aList[i]    #return the original

def randomBinaryList(n):
    """ Generates list of random 1s and 0s
        Args:
            n (int): length of desired list
        Returns:
            list: List of randomly generated 1s and 0s
    """       
    if n == 0:
        return []
    else:
        return [choice([0, 1])] + randomBinaryList(n - 1)

#new version of evolve    
def evolve(aList):
    """evolve takes in a list of integers, aList,
        and returns a new list of integers
        considered to be the "next generation"
    """
    n = len(aList)    #n now holds the size of the list aList
    x = choice(range(len(aList)))    #Get numeric input from user
    return [setNewElement(aList, i, x) for i in range(n)]



    
    
    






# Note: the code below is for the optional
#       graphics part of this lab.
# Feel free to ignore - at least til then.
#
# Mac OS X users likely need to uncomment
# the done() line at the very bottom here.


from turtle import *
import csgrid; from csgrid import *
from random import *

def runGraphicsGen(aList, col):
    """ aList is the list last displayed
        evolve aList first
    """
    print("col is", col)
    aList = evolve(aList, col)
    show(aList)             # display
    if isAllOnes(aList):
        print("Hooray!")
        return

    # We finish here!

    # When the mouse is clicked,
    # this will be called again!

    # aList is "remembered" by show (in a "global"
    # variable) and is later passed in by the
    # graphics system. Global variables are
    # best avoided, but sometimes are required.

def evolve(aList, x):
    """ evolve takes in a list of integers, aList,
          and returns a new list of integers
          considered to be the "next generation"
    """
    N = len(aList)  # N now holds the size of the list aList
    return [setNewElement(aList, i, x) for i in range(N)]

def setNewElement(aList, i, x):
    """ setNewElement returns the NEW list's ith element
          input aList: any list of integers
          input i: the index of the new element to return
          input x: an extra, optional input for future use
    """
    if abs(i-x)<=1:  # if it's the user's chosen column,
        return 1-aList[i]            # toggle the one clicked
    else:                        # otherwise,
        return aList[i]              # return the original



# set the mouse handler...
def mouseHandler(x, y):
    """ This function is called with each mouse click.

        Its inputs are the pixel location of the
        next mouse click: (x, y)

        It computes the column (within the list)
        where the click occurred with getCol.

        The overall list is shared between turtle graphics
        and the other parts of your program as a global
        variable named currentL. In general, global variables
        make software more complex, but sometimes they are
        necessary.

        Then, this function calls the next generation via
        runGraphicsGen(aList, col) - note that the col is available!
    """
    col = getCol(x, y)
    aList = csgrid.currentL  # get from the graphics module
    runGraphicsGen(aList, col)

onscreenclick(mouseHandler)

# here is where your starting conditions go...
# when it runs, it will be ready to play
# however, you'll need to change the setNewElement function, above
# in order to play according to the "Lights out" rules...

startingList = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
show(startingList)

#done()  # your system may need this line uncommented...

