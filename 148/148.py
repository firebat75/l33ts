class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(head):

    if not head:
        return None

    temp = []
    while head:
        temp.append(head.val)
        head = head.next

    temp.sort()

    output = ListNode(temp[0])
    head = output

    for num in temp[1:]:
        output.next = ListNode(num)
        output = output.next
        

    return head

