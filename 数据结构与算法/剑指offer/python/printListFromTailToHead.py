class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printListFromTailToHead(listNode):
        ls = []
        while listNode != None:
            ls.append(listNode.val)
            listNode = listNode.next
        return ls[::-1]

if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    printListFromTailToHead(node)
