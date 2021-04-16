def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    overlappingIntervals = []
    left = sortedIntervals[0][0]
    right = sortedIntervals[0][1]
    for i in range(1, len(sortedIntervals)):
        if right >= sortedIntervals[i][0]:
            right = max(right, sortedIntervals[i][1])
        else:
            overlappingIntervals.append([left, right])
            left, right = sortedIntervals[i][0], sortedIntervals[i][1]
    overlappingIntervals.append([left, right])
    return overlappingIntervals
