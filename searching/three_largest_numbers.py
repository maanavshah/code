# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    if not threeLargest[2] or num > threeLargest[2]:
        shiftLargest(threeLargest, num, 2)
    elif not threeLargest[1] or num > threeLargest[1]:
        shiftLargest(threeLargest, num, 1)
    elif not threeLargest[0] or num > threeLargest[0]:
        shiftLargest(threeLargest, num, 0)


def shiftLargest(threeLargest, num, idx):
    while idx >= 0:
        threeLargest[idx], num = num, threeLargest[idx]
        idx -= 1
