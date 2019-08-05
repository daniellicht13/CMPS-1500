"""https://www.glassdoor.com/Interview/software-engineer-interview-questions-SRCH_KO0,17.htm"""
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
##
def power(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n
    return n * power(n, p - 1)

'''Given an array of numbers, replace each number with the
product of all the numbers in the array except the number
itself *without* using division.'''
def array(L):
    M = L[:]
    for i in range(len(L)):
        total = 0
        for j in (L[:i] + L[i + 1:]):
            total += j
            M[i] = total
    return M

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def duplicate(string):
    if string == '' or len(string) == 1:
        return 'no duplicate'
    for i in range(len(string)):
        if string[i] not in string[i + 1:]:
            return duplicate(string[i + 1:])
        return string[i]

def removedup(sortedArray): ##works except for duplicates on last index
    output = []
    for i in range(1,len(sortedArray)):
        if sortedArray[i] != sortedArray[i-1]:
            output += [sortedArray[i-1]]
    if sortedArray[len(sortedArray)-1] != sortedArray[len(sortedArray)-2]:
        output += [sortedArray[len(sortedArray)-1]]
    return output
    
    
        
            
