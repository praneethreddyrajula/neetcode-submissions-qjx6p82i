class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hMap = {")":"(",
                "}":"{",
                "]":"["}

        for i in s:
            if i in hMap:
                if stack and stack[-1]==hMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True