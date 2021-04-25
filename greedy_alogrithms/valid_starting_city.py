# O(n^2) time | O(1) space
def remainingFuel(distances, fuel, index):
    n = len(distances)
    i = index
    currFuel = 0
    while i != ((index - 1) % n):
        currFuel += fuel[i] - distances[i]
        if currFuel < 0:
            return False
        i = ((i + 1) % n)
    return True

def validStartingCity(distances, fuel, mpg):
    fuel = [x * mpg for x in fuel]
    for i in range(len(distances)):
        if distances[i] < fuel[i] and remainingFuel(distances, fuel, i):
            return i
