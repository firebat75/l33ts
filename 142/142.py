class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            break
    else:
        return None  # if not (fast and fast.next): return None
    while head != slow:
        head, slow = head.next, slow.next
    return head


def maker(ls):
    x = ListNode(None)
    y = x
    for item in ls:
        temp = ListNode(item)
        y.next = temp
        y = y.next

    return x.next


def looper(ll, index):
    index2 = index
    x = ll
    temp = None
    while x.next:
        x = x.next
        index2 -= 1
        if index2 == 0:
            temp = x

    x.next = temp

    print(f"tail now leads to index {index}: {temp.val}")
    return ll


ll1 = maker(
    [
        -21,
        10,
        17,
        8,
        4,
        26,
        5,
        35,
        33,
        -7,
        -16,
        27,
        -12,
        6,
        29,
        -12,
        5,
        9,
        20,
        14,
        14,
        2,
        13,
        -24,
        21,
        23,
        -21,
        5,
    ]
)
ll1 = looper(ll1, 24)
sol1 = solution(ll1)
print(sol1.val)
