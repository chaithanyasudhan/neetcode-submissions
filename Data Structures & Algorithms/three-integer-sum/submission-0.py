class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        for i in range(n):
            target=0-nums[i]
            a=set()
            for j in range(i+1,n):
                if target-nums[j] in a:
                    t = sorted([nums[i], nums[j], target-nums[j]])
                    if t not in res:
                        res.append(t)
                a.add(nums[j])

        return res
                

        