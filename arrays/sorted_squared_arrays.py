# O(n) time | O(n) space
def sortedSquaredArray(array):
	left = 0
	right = len(array) - 1

	squaredArray = []

	while left <= right:
		if abs(array[left]) > abs(array[right]):
			# prepend the squared value
			squaredArray.insert(0, array[left] * array[left])
			left += 1
		else:
			# prepend the squared value
			squaredArray.insert(0, array[right] * array[right])
			right -= 1
	return squaredArray
