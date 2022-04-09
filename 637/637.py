class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root):
    q, output = [root], []
    while len(q):
        qlen, row = len(q), 0
        for i in range(qlen):
            curr = q.pop(0)
            row += curr.val
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        output.append(row / qlen)
    return output


a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution(a))
b = TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(7))
print(solution(b))
