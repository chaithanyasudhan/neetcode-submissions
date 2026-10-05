class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        d={}
        sum=0
        while l<len(s) :
            if s[l] not in d:
                d[s[l]]=l 
            else:
                r=max(d[s[l]]+1,r)
                d[s[l]]=l
            l+=1
            sum=max(l-r,sum)
        return sum


        