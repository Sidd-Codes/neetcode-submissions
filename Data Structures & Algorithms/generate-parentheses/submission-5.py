class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        def dfs(openP, closeP):
            if closeP > openP:
                return
            if closeP == openP == n:
                ans.append("".join(stack))
                return
            if openP < n:
                stack.append("(")
                dfs(openP + 1, closeP)
                stack.pop()

            if closeP < n:
                stack.append(")")
                dfs(openP, closeP + 1)
                stack.pop()

        dfs(0, 0)
        return ans