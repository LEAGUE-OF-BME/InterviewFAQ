def EntryNodeOfLoop(self, pHead): # 26ms 5732K
    # write code here
    ls = []
    count = 0
    head = pHead
    while True:
        if head == None:
            return None
        if head in ls:
            count = ls.index(head)
            break
        ls.append(head)
        head = head.next
    while count > 0:
        pHead = pHead.next
        count -= 1
    return pHead

def EntryNodeOfLoop(self, pHead): # 21ms 5860K
        # write code here
        count = 0
        p1 = pHead
        p2 = pHead
        while True:
            p2 = p2.next
            if p2 == None:
                return None
            p2 = p2.next
            if p2 == None:
                return None
            p1 = p1.next
            count += 1
            if p1 == p2:
                break
        n = count # 环的长度
        p1 = pHead
        p2 = pHead

        while n > 0:
            p2 = p2.next
            n -= 1

        while True:
            if p2 == p1:
                break
            p2 = p2.next
            p1 = p1.next

        return p1
