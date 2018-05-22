# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        index = 0
        array = range(n)
        while len(array) > 1:
            index = (index+m) % len(array) - 1
            array.pop(index)
            if index == -1:
                index = 0
        return array[0]
