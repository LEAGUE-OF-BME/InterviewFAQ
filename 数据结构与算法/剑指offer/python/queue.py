# -*- coding:utf-8 -*-
class Solution:
    """
    用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
         
    def push(self, node):
        # write code here
        if len(self.stack1) == 0:
            while len(self.stack2):
                self.stack1.append(self.stack2.pop())
        self.stack1.append(node)
         
    def pop(self):
        # return xx
        if not len(self.stack2) == 0:
            return self.stack2.pop()
        else:
            while len(self.stack1) > 1:
                self.stack2.append(self.stack1.pop())
            return self.stack1.pop()
