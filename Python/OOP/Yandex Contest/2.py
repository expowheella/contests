# import sys

# input_counter = sys.stdin.readline().strip()

# array=[]

# for i in range(int(input_counter)):
#     value = int(sys.stdin.readline().strip())
    

class TreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

tree = TreeNode(5)
tree.insert(3)
tree.insert(6)
tree.insert(1)

print(tree.left.left.value)