class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Building a small tree manually
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

print(root)
print(root.left)
print(root.right)



























print("root node",root.value)
print(" left child node of root",root.left.value)
print(" right child node of root",root.right.value)
print("")



