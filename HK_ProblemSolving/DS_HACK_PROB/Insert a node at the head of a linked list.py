#!/bin/python3

import math
import os
import random
import re
import sys

from HK_ProblemSolving.DS_HACK_PROB.LINKED_LIST_PRINTING import SinglyLinkedList


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def print_singly_linked_list(node):
    temp = node
    while temp != None:
        print(temp.data)
        temp = temp.next


# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(head, data):
    if head == None:
        node1 = SinglyLinkedListNode(data)
        head = node1
        return head
    else:
        node1 = SinglyLinkedListNode(data)
        node1.next = head
        head=node1
        return head


if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)
