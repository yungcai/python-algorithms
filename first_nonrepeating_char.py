def firstNonRepeatingChar(str):
    for idx in range(len(str)):
        foundDup = false
        for idx2 in range(len(str)):
            if str[idx] == str[idx2] and idx != idx2
            foundDup = True

        if not foundDup:
            return idx

    return -1