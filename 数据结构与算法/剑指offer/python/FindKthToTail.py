def FindKthToTail(self, head, k):
    # write code here
    num = k
    first = head
    second = head
    while num > 0 and first != None:
        first = first.next
        num -= 1
    if num > 0:
        return None
    while first != None:
        first = first.next
        second = second.next
    return second
