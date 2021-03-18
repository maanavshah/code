# O(nlogn) time | O(1) space
def nonConstructibleChange(coins):
    coins.sort()
    totalChange = 0
    for coin in coins:
        if coin > totalChange + 1:
            return totalChange + 1
        totalChange += coin
    return totalChange + 1
