def longgestPeak(arr):
    longestPeakLength = 0
    i = 1
    while i < len(arr) - 1:
        isPeak = arr[i - 1] < arr[i] and arr[i] > arr[i + 1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftidx >= 0 and arr[leftIdx] < arr[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(arr) and arr[rightIdx] < arr[rightIdx - 1]:
            rightIdx += 1
        
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    
    return longestPeakLength