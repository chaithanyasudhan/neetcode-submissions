class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f={}
        for i,c in enumerate(nums):
            co=target-c
            if co in f:
                return[f[co],i]
            f[c]=i
        return []