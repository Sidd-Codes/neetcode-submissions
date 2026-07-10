class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        vals = self.keystore.get(key, [])
        l = 0
        r = len(vals) - 1
        while l <= r:
            m = (l + r)//2
            if vals[m][1] <= timestamp:
                ans = vals[m][0]
                l = m + 1
            else:
                r = m - 1

        return ans