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


# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    count = 0
    if head == None:
        new_node = SinglyLinkedListNode(data)
        head = new_node
        return head
    elif head.next == None:
        new_node = SinglyLinkedListNode(data)
        new_node.next = head
        head = new_node
        return head
    else:
        prev = None
        temp = head
        while count != position and temp != None:
            prev = temp
            temp = temp.next
            count = count + 1
        new_node = SinglyLinkedListNode(data)
        new_node.next = temp
        prev.next = new_node
    return head


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head)
