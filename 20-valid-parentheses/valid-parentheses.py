class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        dict = {
        '}' : '{',
        ']' : '[',
        ')': '(',
        }

        for ch in s:
            if ch in dict:
                top = stack.pop() if stack else '#'
                if top != dict[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack 