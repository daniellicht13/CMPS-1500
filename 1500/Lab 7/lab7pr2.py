"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 7 Part 2
04/06/2018"""

import time

def F(n):
    """ Returns the nth Fibonacci number in the Fibonacci
        sequence using recursion.
        Args:
            n (int): place of number to return in Fibonacci sequence
        Returns:
            int: nth Fibonacci number
    """
    if n == 0 or  n == 1:       #base case
        return n
    return F(n - 2) + F(n - 1)  #recursive step


def f(n):
    """ Returns the nth Fibonacci number in the Fibonacci
        sequence using iteration.
        Args:
            n (int): place of number to return in Fibonacci sequence
        Returns:
            int: nth Fibonacci number
    """   
    number = 0
    number1 = 1
    for i in range(n):
        number += number1
        number1 = number - number1
    return number
        

t1 = time.time()
t1_nice = time.ctime(t1)
f(30)
t2 = time.time()
t2_nice = time.ctime(t2)
total_time = t2 - t1
print(total_time)
    
        
