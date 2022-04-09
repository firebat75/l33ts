class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root):

    if not root:
        return 0

    q, level = [root], 1
    while len(q):
        qlen = len(q)
        for i in range(qlen):
            curr = q.pop(0)
            if not curr.left and not curr.right:
                return level
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        level += 1

    return level


a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution(a))
b = TreeNode(
    2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))
)
print(solution(b))
