class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        a={}
        for i in range(len(numbers)):
            if target-numbers[i] in a:
                res.append(a[target-numbers[i]]+1)
                res.append(i+1)
            else:
                a[numbers[i]]=i
        return res
