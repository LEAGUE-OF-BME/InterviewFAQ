# -*- coding:utf-8 -*-
class Solution:
    """
    请实现一个函数用来找出字符流中第一个只出现一次的字符。
    例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
    当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
    如果当前字符流没有存在出现一次的字符，返回#字符。
    """
    def __init__(self):
        self.dic = {}
        self.s = ""
    # 返回对应char
    def FirstAppearingOnce(self):
        for c in self.s:
            if c in self.dic and self.dic[c] == 1:
                return c
        return '#'
        # write code here
    def Insert(self, char):
        # write code here
        ls = list(self.s)
        ls.append(char)
        self.s = ''.join(ls)
        if char in self.dic:
            self.dic[char] +=1
        else:
            self.dic[char] = 1
