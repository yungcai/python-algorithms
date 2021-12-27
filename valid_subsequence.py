def isValidSubsequence(arr, seq):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(arr) and seqIdx < len(seq):
        if arr[arrIdx] == seq[seqIdx]:
            seqIdx += 1
        arrIdx+= 1
    return seqIdx == len(seq)