# -*- coding:utf-8 -*-
class Solution:
    """
    请实现一个函数用来匹配包括'.'和'*'的正则表达式。
    模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
    在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
    """
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(pattern) == 0 and len(s) == 0:
            return True
        elif len(pattern) > 0 and len(s) == 0:
            if len(pattern) > 1 and pattern[1] == "*":
                return self.match(s, pattern[2:])
            else:
                return False
        elif len(pattern) == 0 and len(s) > 0:
            return False
        else:
            if pattern[0] == s[0]:
                if len(pattern)>1 and pattern[1] == '*':
                    # a*不匹配，a*匹配s[0]
                    return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
                return self.match(s[1:], pattern[1:])
            else:
                if pattern[0] == '.':
                    if len(pattern)> 1 and pattern[1] == '*':
                        # a*不匹配，a*匹配s[0]
                        return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
                    return self.match(s[1:], pattern[1:])
                elif len(pattern) > 1 and pattern[1] == '*':
                    return self.match(s, pattern[2:])
                else:
                    return False
