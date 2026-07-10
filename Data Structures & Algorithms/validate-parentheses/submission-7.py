class Solution:
    def isValid(self, s: str) -> bool:
        pars = { ')':'(', '}':'{', ']':'['}
        stack = []
        for curr in s:
            if curr in pars:
                if len(stack) == 0:
                    return False
                if pars[curr] != stack.pop():
                    return False
            else:
                stack.append(curr)
        return len(stack) == 0