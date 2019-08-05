"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 6 Part 2
03/21/2018"""

 
def selection_sort(aList):
  """Sorts a list in ascending order using the selection sort algorithm.
  """
  n = len(aList)
  for i in range(n - 1):
    
      
    #Find the minimum element in the unsorted portion of the list
    
    smallNdx = i # assume the ith element is the smallest.
    
    #Determine if any other element contains a smaller value.
    for j in range(i + 1, n):
      if aList[j] < aList[smallNdx]:
        smallNdx = j

    # Swap the ith value and smallNdx value  
                      
    tmp = aList[i]
    aList[i] = aList[smallNdx]
    aList[smallNdx] = tmp

  return aList  


def merge_sort(aList):
    """
    Merge sort recursively divide the list into half, sort both halves
    and then merge the two sorted lists into one.
    """
    #If the aList is size 0 or 1, it's already sorted.
    if len(aList) <= 1:
        return aList

    else:
        mid = len(aList) // 2

        # Recursively sort the left and right halves
        left = merge_sort(aList[:mid])
        right = merge_sort(aList[mid:])
        
        # Merge the two (each sorted) parts back together
        return merge(left, right)


                                
def merge(left, right):
    """
    Merge to sorted list, left and right, into one sorted list.
    """
    aList = []
    lt = 0
    rt = 0

    #Repeatedly move the smallest of left and right to the new list
    while lt < len(left) and rt < len(right):
        if left[lt] < right[rt]:
            aList.append(left[lt])
            lt += 1
        else:
            aList.append(right[rt])
            rt += 1

    #There will only be elements left in one of the original two lists.

    #Append the remains of left (lt..end) on to the new list.
    while lt < len(left):
        aList.append(left[lt])
        lt += 1
         
    #Append the remains of right (rt..end) on to the new list.
    while rt < len(right):
        aList.append(right[rt])
        rt += 1

    return aList

def use_mergesort(inputfile, outputfile):
    """Takes an input file of integers and uses mergesort to create a
    new sorted file.
    Args:
        inputfile (str): Input file with list of integers
        outputfile (str): Output file with sorted list of integers
    Returns:
        None
    """
    f = open(inputfile, 'r')
    text = f.read()
    f.close
    numList = text.split()
    for i in range(len(numList)):
        numList[i] = int(numList[i])
    sorted_list = merge_sort(numList)
    output = ''
    for i in range(len(numList)):
        output += str(sorted_list[i]) + '\n'
    g = open(outputfile, 'w')
    g.write(output)
    g.close()
    return

def use_selection(inputfile, outputfile):
    """Takes an input file of integers and uses selection sort to create a
    new sorted file.
    Args:
        inputfile (str): Input file with list of integers
        outputfile (str): Output file with sorted list of integers
    Returns:
        None
    """
    f = open(inputfile, 'r')
    text = f.read()
    f.close
    numList = text.split()
    for i in range(len(numList)):
        numList[i] = int(numList[i])
    selection_sort(numList)
    output = ''
    for i in range(len(numList)):
        output += str(numList[i]) + '\n'
    g = open(outputfile, 'w')
    g.write(output)
    g.close()
    return

import random
random.seed(0)

def generate_nums(filename, n):
    """Makes a file and writes n random numbers from 0 to 99, inclusive.
    Args:
        filename (str): Output file with list of random integers
        n (int): Number of random integers
    Returns:
        None
    """
    text = ''
    for i in range(n):
        num = random.randrange(0, 100)
        text += (str(num) + '\n')
    f = open(filename, 'w')
    f.write(text)
    f.close()
    return
    
    
    
    
    


    
    
