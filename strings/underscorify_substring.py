def underscorifySubstring(string, substring):
    currIdx = [0, None]
    subIdx = 0
    string = list(string)
    for i, s in enumerate(string):
        if s == substring[subIdx]:
            subIdx += 1
            if subIdx == len(substring):
                currIdx[1] = i
                subIdx = 0
        else:
            if currIdx[1]:
                string.insert(currIdx[1]+1, '_')
                string.insert(currIdx[0], '_')
                currIdx[1] = None
            currIdx[0] = i+1
            subIdx = 0
    if currIdx[1]:
        string.insert(currIdx[1]+1, '_')
        string.insert(currIdx[0], '_')
    return ''.join(string)


print(underscorifySubstring('teste testesteste  abab  ', 'teste'))
print(underscorifySubstring('teste', 'teste'))
