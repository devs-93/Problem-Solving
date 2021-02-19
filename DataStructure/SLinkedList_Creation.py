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
        else:
            nodepointer = self.head
            while True:
                if (nodepointer.next==None):
                    print(nodepointer.data,end=' ')
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
    def AtBegining(self,newNode):
        NewNode = newNode
        if self.head!=None:
            NewNode.next=self.head
            self.head=NewNode
        else:
            self.head=NewNode


################################################################
#Inserting at the End of the Linked List
################################################################
#This involves pointing the next pointer of the the current
#last node of the linked list to the new data node. So the
#current last node of the linked list becomes the second last data
#node and the new node becomes the last node of the linked list.
################################################################
    def AtEnd(self,newNode):
        NewNode = newNode
        if self.head==None:
            NewNode.next=self.head
            self.head=NewNode
        else:
            tres=self.head
            while tres.next!=None:
                tres=tres.next
            tres.next=NewNode

########################################################################
#Inserting in between two Data Nodes
########################################################################
#This involves chaging the pointer of a specific node to point to the new node.
#That is possible by passing in both the new node and the existing node
#after which the new node will be inserted. So we define an additional
#class which will change the next pointer of the new node to the next
#pointer of middle node.
#Then assign the new node to next pointer of the middle node.
        # Function to add node
    def Inbetween(self, new_node, AfterWantToInsert):
        tres_node=self.head
        if tres_node is None:
            print("The Linked List is Empty...")
            return
        elif tres_node.next != None:
            while True:
                if tres_node.data==AfterWantToInsert:
                    lastnext=tres_node.next
                    tres_node.next=new_node
                    new_node.next=lastnext
                    break
                elif tres_node.next==None:
                    print('No middle element found!!!!')
                    break
                else:
                    tres_node=tres_node.next



print("#################################################################")
print('Please Enter How Many Element You want to insert.....: ')
print("#################################################################")
n = int(input())
l=SLinkedList()

print("#################################################################")
print('Node Insertion is in progress...')
print("#################################################################")
for i in range(0,n):
    n=Node(input("Please Enter {} th node data \n".format(i)))
    l.insert(n)



print("#################################################################")
print('Now Start insertion in beginng....')
print("\n#################################################################")


print("#################################################################")
print('Please Enter How Many Element You want to insert.....: ',end= ' ')
print("\n#################################################################")
fn = int(input())
for i in range(0,fn):
    n=Node(input("Please Enter {} th node data \n".format(i)))
    l.AtBegining(n)



print("#################################################################")
print('Now Start insertion in End....')
print("\n#################################################################")

print("#################################################################")
print('Please Enter How Many Element You want to insert.....: ',end= ' ')
print("\n#################################################################")
fn = int(input())
for i in range(0,fn):
    n=Node(input("Please Enter {} th node data \n".format(i)))
    l.AtEnd(n)



print("#################################################################")
print('Now Start between two Data Nodes....')
print("\n#################################################################")

print("#################################################################")
print('Please Enter How Many Element You want to insert.....: ',end= ' ')
print("\n#################################################################")
fnb = int(input())
for i in range(0,fnb):
    n1=Node(input("Please Enter {} th node data \n".format(i)))
    n2=input("Please Enter data after you want to insert \n".format(i))
    l.Inbetween(n1,n2)





print("#################################################################")
print("#################-------->OUTPUT<------##########################")
print("#################################################################")
l.printLinkedList()





