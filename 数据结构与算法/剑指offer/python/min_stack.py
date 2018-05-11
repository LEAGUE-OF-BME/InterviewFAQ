# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.ls = []

    def push(self, node):
        # write code here
        self.ls.append(node)
    def pop(self):
        # write code here
        return self.ls.pop()
    def top(self):
        # write code here
        if len(self.ls) == 0:
            return None
        return self.ls[-1]
    def min(self):
        # write code here
        return min(self.ls)
