"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 6 Part 0
02/05/2018"""

'''This program contains two functions used to determine whether lists
of numbers are sorted.
'''

def is_sorted(aList):
    """Returns True if a list is in increasing order and
    False if not.
    Args:
        aList (list): List of numbers
    Returns:
        True (bool): If in increasing order
        False (bool): If not in increasing order
    """
    if len(aList) <= 1:
        return True
    if aList[0] < aList[1]:
        return is_sorted(aList[1:])
    else:
        return False
    
def is_file_sorted(filename):
    """Returns True if a file of numbers is in increasing order and
    False if not.
    Args:
        filename (str): File of numbers
    Returns:
        True (bool): If in increasing order
        False (bool): If not in increasing order
    """
    f = open(filename, 'r')
    text = f.read()
    f.close
    numList = text.split()
    for i in range(len(numList)):
        numList[i] = int(numList[i])
    return is_sorted(numList)


