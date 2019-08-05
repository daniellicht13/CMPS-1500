def sumDigits(st):
    if st == '':
        return 0
    return int(st[0]) + sumDigits(st[1:])

def min_element(root):
    if root == None or root.left == None:
        return root
    return min_element(root.left)

def reverse(string):
    if string == '':
        return string
    return string[-1] + reverse(string[0:-1])

def eat(x):
    x[1] = 9
    x[3] = 11

def prob3():
    food = [4, 5, 6, 7]
    eat(food)
    print('food =', food)

def create2DArray(height, width):
    x = []
    y = []
    for i in range(width):
        for j in range(height):
            x[i] = i * j
        

    y += x
    return y


class Phonebook:
    def __init__(self, name, number):
        self.name = name
        self.number = int(number)
        self.phonebook = {self.name: self.number}

    def __str__(self):
        return str(self.phonebook)

    def isNamePresent(self, name):
        if name in self.phonebook.keys():
            return True
        return False

    def numberFor(self, name):
        if self.isNamePresent(name) == False:
            return -1
        return self.phonebook[name]

    def newContact(self, name, number):
        self.phonebook[name] = number


def myLen(string):
    if len(string) == 0:
        return 0
    return 1 + myLen(string[1:])

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Width: ' + str(self.width) + ' height: ' + str(self.height)

    def area(self):
         self.area = int(self.width) * int(self.height)
         return self.area
        
    def equals(self, other):
        if self.height == other.height and self.width == other.width:
            return True
        return False

    def isSquare(self):
        if self.height == self.width:
            return True
        return False

def remove(x, s):
    if len(s) == 0:
        return s
    if s[0] != x:
        return s[0] + remove(x, s[1:])
    return remove(x, s[1:])



import random
def randomNumber(string):
    x = string[random.randrange(len(string))]
    print(x)

def binarySearch(x,L):
    mid = len(L)// 2
    if len(L) == 1 and L[0] != x:
        return False
    if x == L[mid]:
        return True
    elif x > L[mid]:
        return binarySearch(x, L[mid:])
    elif x < L[mid]:
        return binarySearch(x, L[:mid])

def linearSearch(x,L):
    for i in range(len(L)):
        if L[i] == x:
            return True
    return False

class Node:
    def __init__(self,data):
       self.data = data
       self.next = None      

    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self,data):
        newnode = Node(data)
        self.head = newnode
        self.next = None
        self.tail = newnode

    def __str__(self):
        output = ''
        node = self.head
        while node != None:
            output += str(node) + '--> '
            node = node.next
        return output + 'None'
    
    def traverse(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

    def __append__(self, data):
        currentnode = Node(data)
        if self.head == None:
            self.head = currentnode
            return
        else:
            self.tail.next = currentnode
        self.tail = currentnode


    def __remove__( self, data):
        currentnode = Node(data)
        if self.head == None:
            return
        current = self.head
        while current.next.data != currentnode.data:
            current = current.next
            if current.next == None:
                return False
        current.next = current.next.next

    def find(self, data):
        currentnode = Node(data)
        if self.head == None:
            return False
        current = self.head
        while current.next.data != currentnode.data:
            current = current.next
            if current.next == None:
                return False
        return True


##PRAC TEST
    
def createDictionary():
    d = {'verano':'summer', 'invierno':'winter'}
    return d

def lookup(d,w):
    if w in d.keys():
        return d[w]
    return ''

def Dictionary():
    command = input()
    while command != 'quit':
        print(lookup(createDictionary(),command))
        command = input()
    return

def mystery(aList):
    if len(aList) == 0:
        return aList
    else:
        return mystery(aList[1:]) + aList[0:1]


def sumdigits(string):
    if len(string) == 0:
        return 0
    return int(string[0]) + sumdigits(string[1:])
