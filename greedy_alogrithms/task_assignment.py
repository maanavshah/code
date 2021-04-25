# O(nlogn) time | O(n) space
def taskAssignment(k, tasks):
    h = {}
    for i in range(len(tasks)):
        if tasks[i] not in h:
            h[tasks[i]] = []
        h[tasks[i]].append(i)
    results = []
    tasks.sort()
    for i in range(k):
        results.append([h[tasks[i]].pop(), h[tasks[2 * k - 1 - i]].pop()])
    return results
