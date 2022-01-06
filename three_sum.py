def threeSum(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            currentSum = arr[i] + arr[left] + arr[right]
            if currentSum == target:
                triplets.append(arr[i], arr[left], arr[right])
                left += 1
                right -= 1
            elif currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
    return triplets