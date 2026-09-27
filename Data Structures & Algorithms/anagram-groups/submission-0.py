class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f={}
        for i in strs:
            k="".join(sorted(i))
            if k not in f:
                f[k]=[i]
            else:
                f[k].append(i)
        l=[]
        for i in f:
            l.append(f[i])
        return l