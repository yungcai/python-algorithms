def binarySearch(arr, target):
    return binarySearchHelper(arr, target, 0, len(arr) - 1)

def binarySearchHelper(arr, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = arr[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(arr, target, left, middle - 1)
    else:
        return binarySearchHelper(arr, target, middle + 1, right)
