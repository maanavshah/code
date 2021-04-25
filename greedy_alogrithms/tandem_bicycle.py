# O(nlogn) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    totalLength = len(redShirtSpeeds)
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    totalSpeed = 0
    if fastest:
        for i in range(totalLength):
            totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[totalLength - i - 1])
    else:
        for i in range(totalLength):
            totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return totalSpeed
