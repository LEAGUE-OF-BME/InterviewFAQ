def PrintMinNumber(numbers):
    #https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
    # write code here
    if len(numbers) == 0:
        return ''
    numbers = [str(x) for x in numbers]
    numbers.sort(cmp=lambda x,y: cmp(x+y, y+x))
    return ''.join(numbers).lstrip('0')

if __name__ == '__main__':
    seq = [4,32,325,0]
    print(PrintMinNumber(seq))
