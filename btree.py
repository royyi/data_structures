# Roy Yi
# 9/21/21
# Insert into a binary search tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertBST(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insertBST(root.left, data)
    else:
        root.right = insertBST(root.right, data)
        
    return root

# inorder traversal
def dfs(node):
    if node is None: return
    
    dfs(node.left)
    print(node.data)
    dfs(node.right)

def main():
    root = None
    for x in [12, 4, 9, 10, 18, 15, 19, 3, 7]:
        root = insertBST(root, x)

    dfs(root)

if __name__ == "__main__":
    main()
