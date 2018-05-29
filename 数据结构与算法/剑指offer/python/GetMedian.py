# -*- coding:utf-8 -*-
class Solution:
    """
    如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    排序实现：插入复杂度O(1), 得到中位数复杂度O(nlogn)
    """
    def __init__(self):
        self.ls = []

    def Insert(self, num):
        # write code here
        self.ls.append(num)
    def GetMedian(self, flag=True):
        # write code here
        self.ls.sort()
        n = len(self.ls)
        if n % 2 == 0:
            return (self.ls[n/2] + self.ls[n/2 -1]) / 2.0
        else:
            return self.ls[n/2]

# -*- coding:utf-8 -*-
class SolutionHeap:
    """
    维护最大堆、最小堆，保证最大堆中的数小于最小堆中的所有数
    插入复杂度O(logn), 得到中位数复杂度O(1)
    """
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def max_heapify(self):
        n = len(self.max_heap)
        k = n - 1
        while k > 0 and self.max_heap[(k-1)/2] < self.max_heap[k]:
            self.max_heap[(k-1)/2], self.max_heap[k] = self.max_heap[k], self.max_heap[(k-1)/2]
            k = (k-1) / 2

    def min_heapify(self):
        n = len(self.min_heap)
        k = n - 1
        while k > 0 and self.min_heap[(k-1)/2] > self.min_heap[k]:
            self.min_heap[(k-1)/2], self.min_heap[k] = self.min_heap[k], self.min_heap[(k-1)/2]
            k = (k-1) / 2

    def del_max(self):
        self.max_heap[0], self.max_heap[-1] = self.max_heap[-1], self.max_heap[0]
        val = self.max_heap.pop()
        k = 0
        while 2*k + 1 < len(self.max_heap):
            j = 2*k + 1
            if j + 1 < len(self.max_heap) and self.max_heap[j] < self.max_heap[j+1]:
                j += 1
            if self.max_heap[k] < self.max_heap[j]:
                self.max_heap[k], self.max_heap[j] = self.max_heap[j], self.max_heap[k]
                k = j
            else:
                break
        return val

    def del_min(self):
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        val = self.min_heap.pop()
        k = 0
        while 2*k + 1 < len(self.max_heap):
            j = 2*k + 1
            if j + 1 < len(self.max_heap) and self.max_heap[j] > self.max_heap[j+1]:
                j += 1
            if self.max_heap[k] > self.max_heap[j]:
                self.max_heap[k], self.max_heap[j] = self.max_heap[j], self.max_heap[k]
                k = j
            else:
                break
        return val

    def Insert(self, num):
        # write code here
        if len(self.min_heap) == 0:
            self.min_heap.append(num)
            self.min_heapify()
            return

        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            # 偶数插入最小堆
            if num < self.max_heap[0]:
                a = self.del_max()
                self.max_heap.append(num)
                self.max_heapify()
                self.min_heap.append(a)
                self.min_heapify()
            else:
                self.min_heap.append(num)
                self.min_heapify()
        else:
            # 奇数插入最大堆
            if num > self.min_heap[0]:
                a = self.del_min()
                self.min_heap.append(num)
                self.min_heapify()
                self.max_heap.append(a)
                self.max_heapify()
            else:
                self.max_heap.append(num)
                self.max_heapify()

    def GetMedian(self, flag=True):
        # write code here
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return self.min_heap[0]

if __name__ == '__main__':
    solution = Solution()
    for i in range(5):
        solution.Insert(i)
        print(solution.GetMedian())
