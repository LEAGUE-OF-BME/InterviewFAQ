# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)
        for i, c in enumerate(s):
            if c == ' ':
                s[i] = '%20'
        return ''.join(s)
