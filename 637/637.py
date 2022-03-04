class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root) -> list[float]:
    if not root.right and not root.left: #if node is a leaf
        return [root.val]                #return node value

    else:
        if root.left:


