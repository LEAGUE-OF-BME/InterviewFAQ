# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        """
        请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
        例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
        但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
        """
        # write code here
        def isNum(ls):
            """
            判断是否为不带E的数字
            """
            print(ls)
            if len(ls) == 0:
                return False
            if ls.count('.') > 1:
                return False
            for i, c in enumerate(ls):
                if c < '0' or c > '9':
                    if (c == '+' or c == '-') and i == 0:
                        continue
                    elif c == '.' and i > 0 and i < len(ls)-1:
                        continue
                    else:
                        return False
            return True

        def isInt(ls):
            """
            判断是否为整数
            """
            if len(ls) == 0:
                return False
            for i, c in enumerate(ls):
                if c < '0' or c > '9':
                    if c == '+' or c == '-' and i == 0:
                        continue
                    else:
                        return False
            return True

        if len(s) == 0:
            return False
        ls = s.lower().split('e')
        if len(ls) == 1:
            return isNum(list(ls[0]))
        else:
            return isNum(list(ls[0])) and isInt(list(ls[1]))

if __name__ == '__main__':
    solution = Solution()
    print solution.isNumeric("1+23")
