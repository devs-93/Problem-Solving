import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')
        node = node.next
        if node:
            print(sep, end='')


def reversePrint(head):
    temp = head
    l=[]
    while temp!= None:
        l.append(temp.data)
        temp = temp.next
    n=len(l)
    while n!=0:
        print(l[n-1])
        n=n-1



if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        reversePrint(llist.head)
