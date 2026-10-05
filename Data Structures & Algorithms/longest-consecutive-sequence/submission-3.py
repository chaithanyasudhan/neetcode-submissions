class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=0
        n=set(nums)
        for i in n:
            if i-1 not in n:
                a=1
                while i+a in n:
                    a+=1
                s=max(s,a)
        return s