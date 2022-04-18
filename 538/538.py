class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(node, level=0):
    if node != None:
        # printTree(node.left, level + 1)
        # print(" " * 4 * level + "-> " + str(node.val))
        # printTree(node.right, level + 1)
        printTree(node.right, level + 1)
        print(" " * 4 * level + "-> " + str(node.val))
        printTree(node.left, level + 1)


def solution(root):
    # temp = root

    # def convert(temp, carry=0):
    #     print(temp.val, carry)
    #     print("N##################N")
    #     printTree(root)
    #     print("N##################N")

    #     if not temp.right:
    #         print("bottom" + str(carry))
    #         temp.val += carry
    #         return temp.val
    #     else:
    #         carry += convert(temp.right, carry)
    #         print(carry)
    #         temp.val += carry
    #         print("R##################R")
    #         printTree(root)
    #         print("R##################R")

    #     if temp.left:
    #         convert(temp.left, carry)
    #         print("L##################L")
    #         printTree(root)
    #         print("L##################L")

    # print("--------------------")
    # printTree(temp)
    # print("### " + str(temp.val))
    # print("--------------------")
    # if not temp.right:
    #     print("BOTTOMED RIGHT, VAL: " + str(temp.val))
    #     return temp.val
    # else:
    #     print(temp.val)
    #     rv = convert(temp.right)
    #     print(temp.val, rv)
    #     temp.val += rv
    #     print("summed val R: " + str(temp.val))
    #     print("####################")
    #     printTree(root)
    #     print("####################")
    # if not temp.left:
    #     print("BOTTOMED LEFT, VAL: " + str(temp.val))
    #     return temp.val
    # else:
    #     print(temp.val)
    #     temp.left.val += temp.val
    #     convert(temp.left)
    #     print("####################")
    #     printTree(root)
    #     print("####################")

    sum = 0

    def convert(root):
        nonlocal sum
        if root:
            convert(root.right)
            root.val += sum
            sum = root.val
            convert(root.left)
        return root

    return convert(root)


tree1 = TreeNode(
    4,
    TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, TreeNode(3, None, None))),
    TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, TreeNode(8, None, None))),
)
tree2 = TreeNode(0, None, TreeNode(1, None, None))


printTree(solution(tree1))
printTree(solution(tree2))
