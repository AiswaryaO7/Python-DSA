# maximum depth of binary search
# leedcode104
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create object and call function
obj = Solution()
print("Maximum Depth of Binary Tree:", obj.maxDepth(root))

## invert  binary tree
## 226
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root
def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original Tree (Preorder):")
preorder(root)

obj = Solution()
root = obj.invertTree(root)

print("\nInverted Tree (Preorder):")
preorder(root)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        cur_level_nodes = [root]
        next_level_nodes = []
        cur_level_vals = []
        ans = []

        while cur_level_nodes:
            cur_node = cur_level_nodes.pop(0)
            cur_level_vals.append(cur_node.val)

            if cur_node.left:
                next_level_nodes.append(cur_node.left)

            if cur_node.right:
                next_level_nodes.append(cur_node.right)

            if not cur_level_nodes:
                ans.append(cur_level_vals[:])
                cur_level_vals = []
                cur_level_nodes = next_level_nodes[:]
                next_level_nodes = []

        return ans

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
obj = Solution()
print("Level Order Traversal:")
print(obj.levelOrder(root))