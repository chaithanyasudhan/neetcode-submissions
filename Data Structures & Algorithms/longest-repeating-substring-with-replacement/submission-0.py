class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0#left pointer
        f = {}
        res = 0
        maxf = 0

        for r in range(len(s)):#right pointer for sliding window
            f[s[r]] = f.get(s[r], 0) + 1#storing freq
            maxf = max(maxf, f[s[r]])#keep updating maxf at each shift to right
            while(r-l+1)-maxf>k:#while the window is invalid
                f[s[l]]-=1
                l+=1# keep shrinking from left
            res=max((r-l+1),res)   
        return res
            
        
            