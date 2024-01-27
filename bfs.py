class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first_search(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result

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

print("Breadth-First Traversal:", breadth_first_search(root))
