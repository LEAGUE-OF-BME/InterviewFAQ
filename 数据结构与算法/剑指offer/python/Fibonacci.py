# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        a = 0
        b = 1
        while n > 1:
            a, b = b, a+b
            n -= 1
        return b
