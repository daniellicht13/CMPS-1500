"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 9 Part 1
04/18/2018"""

class Node:
    
    def __init__(self, old = None, new = None, next = None):
        self.old = old
        self.new = new
        self.next = None
        
    def __str__(self):
        return str(self.old) + '-->' + str(self.new)
    
    def print_list_pretty(self):
        p = self
        while (p != None):
            print (p.data, "->", end="")
            p = p.next
        print ("None")

def find(L, old_address, new_address):
    p = L
    while (p.old != old_address) and (p.new != new_address):
        p = p.next
        if p == None:
            return False
    return True
            

def ADD(L, old_address, new_address):
    if find(L, old_address, new_address) == True:
        print('Entry already exists!')
        return L
    else:
        p = L
        L = Node(old_address, new_address)
        L.next = p
        print('Added!')
        return L

def REMOVE(L, old_address, new_address):
    if L.old == None:
        print('No such entry!')
        return L
    elif (L.old == old_address) and (L.new == new_address):
        L = L.next
        print('Removed!')
        return L
    p = L
    while (p.next.old != old_address) and (p.next.new != new_address):
        p = p.next
        if p.next == None:
            print('No such entry!')
            return L
    if (p.next.old == old_address) and (p.next.new == new_address):
        p.next = p.next.next
        print('Removed!')
        return L

def MAIL(L, old_address):
    p = L
    if p.old == None:
        print('Send to', old_address)
        return
    while p.old != old_address:
        if p.new == p.next.old:
            p.next = p.next.next
        p = p.next
    print('Send to', p.new)
    return

def QUIT():
    print('Goodbye')
    return  

def Main():
    L = Node()
    command = ''
    while command != 'QUIT':
        command = input()
        if command == 'ADD':
            L = ADD(L, input(),input())
        elif command == 'REMOVE':
            L = REMOVE(L, input(),input())
        elif command == 'MAIL':
            MAIL(L, input())
    QUIT()
    return
            

Main()


    
