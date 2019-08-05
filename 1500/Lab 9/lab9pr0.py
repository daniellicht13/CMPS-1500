"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 9 Part 0
04/18/2018"""


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

def join(head1, head2):
    """ joins two singly-linked lists togehter
        Args:
            head1 (Node): Head of the first linked list
            head2 (Node): Head of the second linked list
        Returns:
            list1 (Node): Head of the new joined list
    """
    list1 = None
    if head1 == None:
            if head2 == None:
                return list1
            else:
                list1 = head2
                return list1
    else:
        if head2 == None:
            list1 = head1
            return list1
        else:
            list1 = head1
            currentnode = list1
            while currentnode.next != None:
                currentnode = currentnode.next
            currentnode.next = head2
            return list1
        
"""Runs O(n - len(second linked list)) because the while loop runs the amount
of objects in the first linked list. It only changes the pointer of the tail
of the first linked list."""


