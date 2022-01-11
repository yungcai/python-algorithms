def smallestDiff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    idx1 = 0
    idx2 = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while idx1 < len(arr1) and idx2 < len(arr2):
        firstNum = arr1[idx1]
        secondNum = arr2[idx2]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idx1 += 1
        elif secondNum < firstNum
        current = firstNum - secondNum
        idx2 += 1
        else: 
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]\
    return smallestPair