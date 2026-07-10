class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            lenStr = int(s[i:j])

            ans.append(s[j+1:j+lenStr + 1])

            i = j + lenStr + 1
        return ans
