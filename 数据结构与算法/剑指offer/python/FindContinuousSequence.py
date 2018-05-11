def FindContinuousSequence(tsum):
    # write code here
    if tsum < 2:
        return []
    results = []
    end = int(tsum / 2) + 1
    for i in range(1, end):
        n = ((i-0.5)**2 + 2*tsum)**0.5 - i + 0.5 # i: 正整数序列第一个数； n: 序列长度 解二次方程得到n
        if n % 1 == 0:
            results.append([x for x in range(i, i+n)])
    return results

if __name__ == '__main__':
    FindContinuousSequence(3)
