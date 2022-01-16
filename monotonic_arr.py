def isMonotonic(arr):
    if len(arr) <= 2:
        return True
    
    direction = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if direction == 0:
            direction = arr[i] - arr[i - 1]
            continue
        if breaksDirection(direction, arr[i - 1], arr[i]):
            return False

    return True

def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0