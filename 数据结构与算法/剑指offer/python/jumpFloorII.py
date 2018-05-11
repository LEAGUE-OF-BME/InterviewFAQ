# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        a = [0] * number
        a[0] = 1
        for i in range(1, number):
            a[i] = sum(a[:i]) + 1
        return a[number - 1]
