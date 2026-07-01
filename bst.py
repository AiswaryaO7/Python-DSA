class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        #insert
    def insert(self,root,key):
            if root is None:
                return Node(key)
            if key<root.data:
                root.left=self.insert(root.left,key)
            elif key>root.data:
                root.right=self.insert(root.right,key)
            return root
    #search
    def search(self,root,key):
            if root is None:
                return False
            if root.data==key:
                return True
            if key<root.data:
                return self.search(root.left,key)
            return self.search(root.right,key)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

    #preorder Traversal
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    #postorder traversal
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")


#-------------------Driver code--------------------------

bst=BST()
values=[50,30,70,20,40,60,80]
for values in values:
    bst.root=bst.insert(bst.root,values)
print("Inorder Traversal" )
bst.inorder(bst.root)
print("Preorder Traversal" )
bst.preorder(bst.root)
print("postorder Traversal" )
bst.postorder(bst.root)

#inorder
    


    
    

