class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans = ans + (str)(len(i))+'#'+i
            print(ans)
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        cnt = 0
        i = 0
        curr = ""
        num = ""
        while i < len(s):
            num = ""
            curr = ""
            while s[i] != '#' and i < len(s):
                num += s[i]
                i += 1
            i += 1
            cnt = int(num)
            while cnt != 0 and i < len(s):
                curr = curr + s[i]
                cnt -= 1
                i += 1
            ans.append(curr)
        return ans