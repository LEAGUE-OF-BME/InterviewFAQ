# -*- coding:utf-8 -*-
class Solution:
    # https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?tpId=13&tqId=11180&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
    # 字符串的排列
    def add(self, ls, ind, result):
        """
        递归确定一个位置的字符
        """
        if ind == len(ls)-1:
            result.append(''.join(ls))
        else:
            for i in range(ind, len(ls)):
                ls[ind], ls[i] = ls[i], ls[ind]
                self.add(ls, ind+1, result)
                ls[ind], ls[i] = ls[i], ls[ind]

    def Permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        ls = list(ss)
        result = []
        self.add(ls, 0, result)
        result = list(set(result))
        result.sort()
        return result
