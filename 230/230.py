class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root, k):

    vals = []

    def helper(root, k):
        nonlocal vals
        print(root.val, vals)
        found = False
        if root.left:
            helper(root.left, k)
        vals.append(root.val)
        if root.right:
            helper(root.right, k)

    helper(root, k)
    return vals[k - 1]


tree1 = TreeNode(3, TreeNode(1, None, TreeNode(2, None, None)), TreeNode(4, None, None))
tree2 = TreeNode(
    5,
    TreeNode(3, TreeNode(2, TreeNode(1, None, None), None), TreeNode(4, None, None)),
    TreeNode(6, None, None),
)
print(solution(tree1, 1))
print(solution(tree2, 3))
