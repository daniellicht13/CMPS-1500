"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 3 Part 0
02/16/2018"""

'''This program asks a user to input two DNA strings, displays a menu option
to a user and allows them to add and delete indels, score the alignment of
their DNA strings, and quit the program'''

'''
    Adds an indel at a at given position
    Args:
        string (str): DNA string
        position (int): position of added indel.
    Returns:
        str: DNA string with added indel
'''

def add(string, position):
    if position <= len(string):
        string = string[0:position] + '-' + string[position:]
    return string

'''
    Deletes an indel at a specified position
    Args:
        string (str): DNA string
        position (int): positiion of deleted indel
    Returns:
        str: DNA string without indel
'''

def delete(string, position):
    if position <= len(string):
        if string[position] == '-':
            string = string[0:position] + string [position + 1:]
    return string

'''
    Verifies if the string consists of 'A', 'T', 'C', and/or 'G'
    Args:
        string (str): DNA string
    Returns:
        bool: True if consists of only 'A', 'T', 'C', and/or 'G'. Otherwise False
'''

def validDNA(string):
    DNA = True
    for i in string:
        if i not in 'ATCG':
            DNA = False
    return DNA

'''
    Compeletes a string with dash so the total length of the string is n
    Args:
        string (str): DNA string
        n (int): desired length of DNA string
    Returns:
        str: DNA string with indel(s) added to end so DNA string is of length n
'''

def fill(string, n):

    if n > len(string):
        return string + '-' * (n-len(string))
    return string

'''
    Determines how many positions in the string have matching charcters
        Args:
            str1 (str): First DNA string
            str2 (str): Second DNA string
        Returns:
            int: Number of matched positions
'''

def score(str1, str2):
    count = 0
    if len(str1) <= len(str2):
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                count += 1
    else:
        for i in range(len(str2)):
            if str2[i] == str1[i]:
                count += 1      
    return count
        
