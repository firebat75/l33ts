class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def solution(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

    if not original:
        return None

    if original.val == target.val:
        return cloned
    
    return solution(original.left, cloned.left, target) or solution(original.right, cloned.right, target)