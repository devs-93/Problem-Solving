class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root is None:
            return 0;

        else:

            # Compute the depth of each subtree
            lDepth = self.getHeight(root.left)
            rDepth = self.getHeight(root.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth + 1
            else:
                return rDepth + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)-1
print(height)