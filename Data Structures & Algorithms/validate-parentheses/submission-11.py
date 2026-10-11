class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        chars = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in chars:
                st.append(chars[i])
            else:
                if st == []:
                    return False
                char = st.pop()
                if char != i:
                    return False
        return True if st == [] else False
        
