class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1
    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        minHeap = []
        if userId not in self.followMap[userId]:
            self.followMap[userId].add(userId)
        if len(self.followMap[userId]) >= 10:
            maxHeap = []
            for i in self.followMap[userId]:
                if i in self.tweetMap:
                    count, tweetId = self.tweetMap[i][-1]
                    heapq.heappush(maxHeap, [-count, tweetId, i, len(self.tweetMap[i])-1])
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index])
        else:
            for i in self.followMap[userId]:
                if i in self.tweetMap:
                    count, tweetId = self.tweetMap[i][len(self.tweetMap[i]) - 1]
                    heapq.heappush(minHeap, [count, tweetId, i, len(self.tweetMap[i]) - 1])
        while minHeap and len(ans) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            ans.append(tweetId)
            if index - 1 >= 0:
                count, tweetId = self.tweetMap[followeeId][index-1]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])  
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)