# O(nd) time | O(n) space
def minNumberOfCoinsForChange(n, denoms):
    minCoins = [float("inf")] * (n + 1)
    minCoins[0] = 0
    for denom in denoms:
        for i in range(n + 1):
            if denom <= i:
                minCoins[i] = min(minCoins[i], minCoins[i - denom] + 1)
    return minCoins[-1] if minCoins[-1] != float("inf") else -1
