class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None

def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swap(current)
        queue.append(current.left)
        queue.apprend(current.right)
    
def swap(tree):
    tree.left, tree.right = tree.right, tree.left