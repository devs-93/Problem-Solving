class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        if lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

    def PrintTree_Inorder(self):
        if self.left:
            self.left.PrintTree_Inorder()
        print(self.data,end=' ')
        if self.right:
            self.right.PrintTree_Inorder()
    def PrintTree_Preorder(self):
        print(self.data,end=' ')
        if self.left:
            self.left.PrintTree_Preorder()
        if self.right:
            self.right.PrintTree_Preorder()
    def PrintTree_Postorder(self):
        if self.left:
            self.left.PrintTree_Postorder()
        if self.right:
            self.right.PrintTree_Postorder()
        print(self.data,end=' ')


insert_root_node = int(input())
root = Node(insert_root_node)
print('Input How Many Element want to insert....')
data = int(input())
i = 0
while i < data:
    root.insert(int(input()))
    i = i + 1
root.PrintTree_Inorder()
print('\n')
root.PrintTree_Preorder()
print('\n')
root.PrintTree_Postorder()
# print('Insert element to want find')
# result=root.findval(int(input()))
# print(result)