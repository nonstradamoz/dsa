class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def dfs(root):
    if root is None:
        return
    
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("DFS Traversal:")
dfs(root)
