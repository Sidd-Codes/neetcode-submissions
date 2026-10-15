class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1 = []
        stack2 = []
        for i in range(len(s)):
            if s[i] == '(':
                stack1.append(i)
            elif s[i] == '*':
                stack2.append(i)
            else:
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False
        while stack1 and stack2:
            if stack1.pop() > stack2.pop():
                return False
        return not stack1