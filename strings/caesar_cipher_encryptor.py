# O(n^2) time | O(n) space
#
# string += 'c'  <- has time complexity O(n^2)
#
def caesarCipherEncryptor(string, key):
    alphaList = list('abcdefghijklmnopqrstuvwxyz')
    cipher = ''
    for s in string:
        cipher += alphaList[(alphaList.index(s) + key) % 26]
    return cipher


# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    cipher = []
    for s in string:
        cipher.append(chr((ord(s) - 97 + key) % 26 + 97))
    return ''.join(cipher)


# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    alphaList = list('abcdefghijklmnopqrstuvwxyz')
    cipher = []
    for s in string:
        cipher.append(alphaList[(alphaList.index(s) + key) % 26])
    return ''.join(cipher)
