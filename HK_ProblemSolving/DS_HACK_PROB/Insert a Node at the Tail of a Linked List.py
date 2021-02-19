
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


def print_singly_linked_list(node):
    while node:
        print(node.data)
        node=node.next


def insertNodeAtTail(head, data):
    temp=head
    if head==None:
        node1 = SinglyLinkedListNode(data)
        head=node1
    else:
        node1=SinglyLinkedListNode(data)
        while temp.next!=None:
            temp=temp.next
        temp.next=node1
    return head


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)
