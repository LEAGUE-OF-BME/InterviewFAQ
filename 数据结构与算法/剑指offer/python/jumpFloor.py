# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 1:
            return 0
        a = [0,1,2]
        for i in range(3, number + 1):
            a.append(a[i-1] + a[i-2])
        return a[number]
