# O(n) time | O(n) space
def balancedBrackets(string):
    bracketPair = {'{': '}', '(': ')', '[': ']'}
    openBrackets = '({['
    closeBrackets = ')}]'
    stack = []
    for s in string:
        if s in closeBrackets:
            if stack:
                if s != bracketPair[stack.pop()]:
                    return False
            else:
                return False
        elif s in openBrackets:
            stack.append(s)
    return False if stack else True
