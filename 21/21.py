class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        x = ""
        curr = self
        while curr:
            x += f"[{str(curr.val)}]->"
            curr = curr.next
        x += "None"
        return x


def mergeTwoLists(list1, list2):
    merged = ListNode()
    curr = merged

    while list1 or list2:
        print("list1: ", list1)
        print("list2: ", list2)
        print("merged: ", merged)

        if not list1:
            curr.next = ListNode(list2.val)
            list2 = list2.next
        elif not list2:
            curr.next = ListNode(list1.val)
            list1 = list1.next

        else:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next

        curr = curr.next

    return merged.next


x1 = ListNode(1, ListNode(2, ListNode(4)))
x2 = ListNode(1, ListNode(3, ListNode(4)))
