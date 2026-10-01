class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for st in strs:
            ans.append(str(len(st)))
            ans.append('#')
            ans.append(st)
        return "".join(ans)
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            ans.append(s[j+1:j+length+1])
            i = j + 1 + length
        return ans
