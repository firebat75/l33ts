def solution(head, n):

    if not head.next:
        return None

    end = head
    temp = head
    for i in range(n):
        end = end.next

    if end:
        while end.next:
            end = end.next
            temp = temp.next

        temp.next = temp.next.next
    else:
        head = head.next
    

    return head