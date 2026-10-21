class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0]*26

        for task in tasks:
            counter[ord(task) - ord('A')] += 1

        counter.sort()
        gaps = (counter[-1] - 1)*n
        for i in range(len(counter)-2, -1, -1):
            gaps -= min(counter[-1] - 1, counter[i])

        return max(0, gaps) + len(tasks)