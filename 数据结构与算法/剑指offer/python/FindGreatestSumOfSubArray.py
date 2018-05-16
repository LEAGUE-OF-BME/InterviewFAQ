# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        num = array[0] # 以当前元素结尾的最大子数组和
        result = array[0] # 当前所有子数组的最大和
        for i in array[1:]:
            num = max(i, num+i)
            result = max(result, num)
            print("num: {}, result:{}".format(num, result))
        return result

if __name__ == '__main__':
    solution = Solution()
    array = [1,-2,3,10,-4,7,2,-5]
    print(solution.FindGreatestSumOfSubArray(array))
