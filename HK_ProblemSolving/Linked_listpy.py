class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        print(current)
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head == None:
            node1 = Node(data)
            head = node1
        else:
            temp = head
            while temp.next != None:
                temp = temp.next
            node2 = Node(data)
            temp.next = node2
        return head

    # Complete this method


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);
