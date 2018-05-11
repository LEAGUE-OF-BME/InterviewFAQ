# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # Python 中，整数是没有范围限制的，不会溢出（overflow），需要人工限定范围。
        INT_BITS = 32
        MAX_INT = (1 << (INT_BITS - 1)) - 1
        count = 0
        while n:
            if n < - MAX_INT- 1 or n > MAX_INT:
                break
            n = n & (n - 1)
            count += 1
        return count
