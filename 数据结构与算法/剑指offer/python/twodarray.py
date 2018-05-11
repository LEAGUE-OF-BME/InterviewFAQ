def Find(target, array):
    # write code here
    while len(array) > 0 and len(array[0]) > 0:
        print(array)
        if array[0][-1] == target:
            return True
        elif array[0][-1] > target:
            # remove column
            array = [a[:-1] for a in array]
        else:
            # remove row
            array = array[1:]

    return False

if __name__ == '__main__':
    target = 7
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(Find(target, array))
