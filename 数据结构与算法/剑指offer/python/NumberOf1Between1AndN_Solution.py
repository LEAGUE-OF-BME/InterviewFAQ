# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        #https://www.nowcoder.com/practice/bd7f978302044eee894445e244c7eee6?tpId=13&tqId=11184&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
        # write code here
        """
        按每一位求，例如12345: 求0-10000，0-2000，0-300，0-40，0-5之和
        a表示除去最高位后的位数
        int(10 ** a * a/10)表示除去最高位后出现1的个数，如果最高位大于1，再加上10**a；如果最高位等于1，再加上此后所有数（10000-12345）
        """
        result = 0
        if n < 0:
            return 0
        length = len(str(n))
        listN = list(str(n))
        for i, v in enumerate(listN):
            a = length - i -1
            if i == length - 1 and int(v) >=1:
                result += 1
                break
            if int(v) > 1:
                result += int(10 ** a * a/10) * int(v) + 10**a
            if int(v) == 1:
                result += (int(10 ** a * a /10) + int("".join(listN[i+1:])) + 1)
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.NumberOf1Between1AndN_Solution(200))
