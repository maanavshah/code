# O(nlogn) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    direction = (redShirtHeights[0] - blueShirtHeights[0]) > 0
    for i in range(len(redShirtHeights)):
        if direction:
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        else:
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
    return True
