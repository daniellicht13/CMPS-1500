"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 7 Part 1
04/06/2018"""

def uppercount(s):
    """ Counts total number of uppercase letters in a string
        Args:
            s (str): string of characters
        Returns:
            int: Number of vowels in s
    """
    if s == '':             #base case
        return 0
    else:                   #recursive step
        if s[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':        
            return 1 + uppercount(s[1:])
        else:
            return uppercount(s[1:])
        
'''When you're going through a list of first and last names you
can get the number of people by dividing the result of uppercount
by 2.
Another example would be if you edit this function to count periods
so you could use it to count the number of sentences in a paragraph.
'''

def clean_string(s):
    """ Deletes all non-letter and non-space characters from string
        Args:
            s (str): string of characters
        Returns:
            string: s without characters that are not letters or spaces
    """           
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
    if s in letters:        #base case
        return s
    else:                   #recursive step
        if s[0] not in letters:
            return clean_string(s[1:])
        else:
            return s[0] + clean_string(s[1:])

def clean_list(l1, l2):
    """ Returns a list of values from l1 that are not in l2
        Args:
            l1 (list): list of elements
            l2 (list): list of elements
        Returns:
            list: list containing all elements from l1 that are not
            in l2.
    """ 
    if l1 == []:            #base case
        return []
    else:                   #recursive step
        if l1[0] in l2:
            return clean_list(l1[1:], l2)
        else:
            return [l1[0]] + clean_list(l1[1:], l2)
