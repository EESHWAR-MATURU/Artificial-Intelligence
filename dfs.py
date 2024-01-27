class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(node):
    if node is None:
        return

    print(node.value)  

    dfs(node.left)    
    dfs(node.right)   

# Example binary tree:
#        1
#       / \
#      2   3
#     / \  / \
#    4  5  6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Depth-First Traversal:")
dfs(root)
