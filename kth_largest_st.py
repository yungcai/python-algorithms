class BST:
    def __inti__(self, value, left = None, right = None):
        self.value = value
        self.left = left 
        self.right = right

def findthLargestValue(tree, k):
    sortedNodeValues = []
    inOrderTraverse(tree, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues) - k]

def inOrderTraverse(node, sortedNodeValues):
    if node is None:
        return 

    inOrderTraverse(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraverse(node.right, sortedNodeValues)