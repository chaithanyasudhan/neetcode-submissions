class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        f=Counter(nums)
        s=[]
        for i in f:
            if len(s)<k:
                heapq.heappush(s,(f[i],i))
            else:
                heapq.heappush(s,(f[i],i))
                heapq.heappop(s)
                
        l=[]
        for i in s:
            l.append(i[1])
        return l
            

