class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(l1, l2):
    s1 = ""
    s2 = ""
    while l1:
        s1 += str(l1.val)
        l1 = l1.next
    while l2:
        s2 += str(l2.val)
        l2 = l2.next
    s1 = s1[::-1]
    s2 = s2[::-1]
    if not s1:
        s1 = "0"
    if not s2:
        s2 = "0"

    n = int(s1) + int(s2)
    n = str(n)
    n = n[::-1]

    output = ListNode(int(n[0]))
    curr = output

    for char in n[1:]:
        curr.next = ListNode()
        curr = curr.next
        curr.val = int(char)
        

    return output