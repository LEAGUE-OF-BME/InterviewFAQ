# -*- coding:utf-8 -*-
class Solution:
    """
    在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
    牛客网上python超时无法通过
    """
    def InversePairs(self, data):
        # write code here
        self.count = 0
        def merge(a, b):
            result = []
            i = 0
            j = 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1
                    self.count += len(a) - i
            result.extend(a[i:])
            result.extend(b[j:])
            return result


        def merge_sort(data):
            if len(data) <= 1:
                return data
            mid = len(data)/2
            left = merge_sort(data[:mid])
            right = merge_sort(data[mid:])
            return merge(left, right)

        merge_sort(data)
        return self.count % 1000000007




if __name__ == '__main__':
    s = Solution()
    data = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301, \
    601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149, \
    588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739, \
    288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973, \
    958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235, \
    187,284,665,874,80,45,848,38,811,267,575]
    print(s.InversePairs(data))
