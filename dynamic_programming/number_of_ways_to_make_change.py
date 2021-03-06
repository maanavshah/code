# O(nd) time | O(n) space
def numberOfWaysToMakeChange(n, denoms):
    ways = [0] * (n + 1)
    ways[0] = 1
    for denom in denoms:
        for i in range(n + 1):
            if denom <= i:
                ways[i] += ways[i - denom]
    return ways[-1]
