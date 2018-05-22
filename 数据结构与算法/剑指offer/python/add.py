# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            s = (num1 ^ num2) & 0xFFFFFFFF # 设置最大位数32
            c = (num1 & num2) << 1
            num1 = s
            num2 = c
        return num1 if num1 <= 0x7FFFFFFF else num1 - 2**32 # 最高位是1表示负数
