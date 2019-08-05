"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 6 Part 1
03/21/2018"""


def main(): #O(1)
    """Prompts user to input file name and outputs a message saying
    whether the file is sorted.
    Args:
        None
    Returns:
        str: Message telling user the file is sorted
        or
        str: Message telling user the file needs to be sorted
    """    
    filename = input('Please enter file name: ') #O(1)
    if is_file_sorted(filename) == False: #O(1)
        print('Looks like', filename, 'needs to be sorted.') #O(1)
    else: #O(1)
        print('Congratulations! The file', filename, 'is nicely sorted!') #O(1)

def is_sorted(aList): #O(1)
    """Returns True if a list is in increasing order and
    False if not.
    Args:
        aList (list): List of numbers
    Returns:
        True (bool): If in increasing order
        False (bool): If not in increasing order
    """
    if len(aList) <= 1: #O(1)
        return True #O(1)
    if aList[0] < aList[1]: #O(1)
        return is_sorted(aList[1:]) #O(1)
    else: #O(1)
        return False #O(1)
    
def is_file_sorted(filename):
    """Returns True if a file of numbers is in increasing order and
    False if not.
    Args:
        filename (str): File of numbers
    Returns:
        True (bool): If in increasing order
        False (bool): If not in increasing order
    """
    f = open(filename, 'r') #O(1)
    text = f.read() #O(1)
    f.close #O(1)
    numList = text.split() #O(1)
    for i in range(len(numList)): #O(n)
        numList[i] = int(numList[i]) #O(1)
    return is_sorted(numList) #O(1)

#Big-Oh running time is O(n)


