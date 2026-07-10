class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        left = 0
        right = len(self.map[key]) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.map[key][mid][1] <= timestamp:
                ans = self.map[key][mid][0] 
                left = mid + 1
            else:
                right = mid - 1
        return ans

