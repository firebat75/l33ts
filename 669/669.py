class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root, low, high):

    if not root.right and not root.left:
        if low <= root.val <= high:
            return root
        else:
            return None
    else:
        

    temp = None
    def helper(temp):
    curr = root


    if low <= root.val <= high:
        temp = TreeNode(root.val)

    if root.left:


    

    elif curr.left:


    return None


tree1 = TreeNode(1, TreeNode(0), TreeNode(2))
print(solution(tree1, 1, 2))
tree2 = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1), None)), TreeNode(4))
print(solution(tree2, 1, 3))
