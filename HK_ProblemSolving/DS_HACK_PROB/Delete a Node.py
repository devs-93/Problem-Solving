#!/bin/python3

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


def print_singly_linked_list(node):
    temp = node
    while temp != None:
        print(temp.data)
        temp = temp.next


# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    count = 0
    if head == None:
        return head
    elif count == position and head.next == None:
        head = None
        return head
    elif count == position and head.next != None:
        head=head.next
        return head
    else:
        temp = head
        prev = None
        while temp != None and count != position:
            count = count + 1
            prev = temp
            temp = temp.next
        prev.next = temp.next
    return head


if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1)
