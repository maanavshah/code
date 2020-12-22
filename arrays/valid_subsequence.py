# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    seqIdx = 0
    seqLength = len(sequence)
    for a in array:
        if a == sequence[seqIdx]:
            seqIdx += 1
            if seqIdx == seqLength:
                return True
    return False

# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for a in array:
        if seqIdx == len(sequence):
            break
        if a == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)
