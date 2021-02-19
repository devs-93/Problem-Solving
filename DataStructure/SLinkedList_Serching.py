class Node:
    def __init__(self, dataval):
        self.data = dataval
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newnode):
        if self.head == None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                else:
                    lastnode = lastnode.next
            lastnode.next = newnode

    #############################
    ##### Traversing
    ##### a
    ##### Linked
    ##### List
    ################################
    def printLinkedList(self):
        if self.head == None:
            print('Linked List is Empty.....')
            return
        else:
            nodepointer = self.head
            while True:
                if (nodepointer.next == None):
                    print(nodepointer.data, end=' ')
                    break
                else:
                    print(nodepointer.data, end=' ')
                    nodepointer = nodepointer.next

    ################################################################
    # Inserting at the Beginning of the Linked List
    ################################################################
    # This involves pointing the next pointer of the new data
    # node to the current head of the
    # linked list. So the current head of the linked list becomes
    # the second data element and the new node becomes the
    # head of the linked list.#######################################
    def AtBegining(self, newNode):
        NewNode = newNode
        if self.head != None:
            NewNode.next = self.head
            self.head = NewNode
        else:
            self.head = NewNode

    ################################################################
    # Inserting at the End of the Linked List
    ################################################################
    # This involves pointing the next pointer of the the current
    # last node of the linked list to the new data node. So the
    # current last node of the linked list becomes the second last data
    # node and the new node becomes the last node of the linked list.
    ################################################################
    def AtEnd(self, newNode):
        NewNode = newNode
        if self.head == None:
            NewNode.next = self.head
            self.head = NewNode
        else:
            tres = self.head
            while tres.next != None:
                tres = tres.next
            tres.next = NewNode

    ########################################################################
    # Inserting in between two Data Nodes
    ########################################################################
    # This involves chaging the pointer of a specific node to point to the new node.
    # That is possible by passing in both the new node and the existing node
    # after which the new node will be inserted. So we define an additional
    # class which will change the next pointer of the new node to the next
    # pointer of middle node.
    # Then assign the new node to next pointer of the middle node.
    # Function to add node
    def Inbetween(self, new_node, AfterWantToInsert):
        tres_node = self.head
        if tres_node is None:
            print("The Linked List is Empty...")
            return
        elif tres_node.next != None:
            while True:
                if tres_node.data == AfterWantToInsert:
                    lastnext = tres_node.next
                    tres_node.next = new_node
                    new_node.next = lastnext
                    break
                elif tres_node.next == None:
                    print('No middle element found!!!!')
                    break
                else:
                    tres_node = tres_node.next

    ########################################################################
    ###########Removing an Item form a Liked List###########################
    ########################################################################
    # '''
    # We can remove an existing node using the key for that node.
    # In the below program we locate the previous node of the node which is to be deleted.
    # Then point the next pointer of this node to the next node of the node to be deleted.
    # '''
    ########################################################################
    # Function to remove node
    def RemoveNode(self, key):
        print('Removal Function......')
        # Store head node
        temp = self.head
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # if key was not present in linked list
        if (temp == None):
            print("ooooooopsssssssssssss!!!!!!")
            return
        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    #####################################################################################
    #################Delete a Linked List node at a given position
    #####################################################################################
    # '''################################################################################
    # Given a singly linked list and a position, delete a linked list node at the given
    # position.
    # '''################################################################################
    # Given a reference to the head of a list
    # and a position, delete the node at a given position
    def deleteNodeAt(self, position):
        # If linked list is empty
        if self.head == None:
            print('No Element in linkedList...')
            return
        # Store head node
        temp = self.head
        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
            # Find previous node of the node to be deleted
        for i in range(0, position - 1):
            temp = temp.next
            if temp is None:
                break

        # If position is more than number of nodes
        if temp is None:
            print('Position is more Than Element')
            return
        if temp.next is None:
            print('Last element in Linked lIst which cant delete .....')
            return
        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next
        temp.next = next
        # print(temp.next.data)

    #############################################################################
    #############################################################################
    # Find Length of a Linked List(Iterative)
    #############################################################################
    # Write a function to count the number of nodes in a given singly linked list.
    #############################################################################
    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        count = 0
        temp = self.head
        if temp is None:
            print('There is no element in list..')
            return
        while temp:
            count = count + 1
            temp = temp.next
        return count

    #####################################################################
    # Search an element in a Linked List(Iterative)
    # Writeafunctionthatsearchesagivenkey ‘x’ in
    # agivensinglylinkedlist.
    # Thefunctionshouldreturn
    # true if x is present in linkedlist and falseotherwise.
    #####################################################################
    def search(self, searching_element):
        # Initialize current to head
        current = self.head
        while current != None:
            if current.data == searching_element:
                return True
            else:
                current = current.next
        return False


#############################################################################
#############################################################################
# Find Length of a Linked List(Recursive)
#############################################################################
# Write a function to count the number of nodes in a given singly linked list.
#############################################################################
# This function counts number of nodes in Linked List
# iteratively, given 'node' as starting node.
# def getCountRec(self, node):
#     if (not node): # Base case
#         return 0
#     else:
#         return 1 + self.getCountRec(node.next)

print("#################################################################")
print('Please Enter How Many Element You want to insert.....: ')
print("#################################################################")
n = int(input())
l = SLinkedList()

print("#################################################################")
print('Node Insertion is in progress...')
print("#################################################################")
for i in range(0, n):
    n = Node(input("Please Enter {} th node data \n".format(i)))
    l.insert(n)

print("#################################################################")
print("#################-------->OUTPUT<------##########################")
print("#################################################################")
l.printLinkedList()
print()
print("Element Count In linked List...: ", l.getCount())
print()

# print("#################################################################")
# print('Node Deletion is in progress...')
# print("#################################################################")
# n = int(input('Number of Element you want to delete.....\n'))
# for i in range(0, n):
#     key = input('Key which you want to delete..\n')
#     n = l.RemoveNode(key)
#     l.printLinkedList()
#     print()


# print("#################################################################")
# print('Node Deletion is in progress...')
# print("#################################################################")
# n = int(input('Number of Element you want to delete.....\n'))
# for i in range(0, n):
#     key = int(input('postion which you want to delete..\n'))
#     n = l.deleteNodeAt(key)
#     l.printLinkedList()
#     print()

print("#################################################################")
print('Node Searching is in progress...')
print("#################################################################")
n = int(input('Number of Element you want to Search.....\n'))
for i in range(0, n):
    key = input('Key which you want to Search..\n')
    n = l.search(key)
    if n == True:
        print('Key Found : ', key)
    else:
        print('Not Exist in LinkedList')
    print()
