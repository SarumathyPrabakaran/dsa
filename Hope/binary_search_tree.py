class BST:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    
    def __init__(self, root_val):
        self.root = self.Node(root_val)
    
    def search_node(self, val):
        
        def helper(curr):

            if val<curr.val and curr.left: return helper(curr.left)
            if val>curr.val and curr.right: return helper(curr.right)
            return curr
        
        return helper(self.root)
    
    def insert(self, val):
        closest = self.search_node(val)
        newNode = self.Node(val)
        if closest.val < val:
            closest.right = newNode
        else:
            closest.left = newNode
    
arr = [1,2,3,4,5,6]
bst = BST(root_val=arr[0])

for i in arr[1:]:
    bst.insert(i)

node = bst.search_node(val=4)
if node.left:
    print(node.left.val)
if node.right:
    print(node.right.val)


if not node.left and not node.right:
    print("-1")

        