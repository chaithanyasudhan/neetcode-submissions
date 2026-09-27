class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        from collections import Counter
        f1=Counter(s)
        f2=Counter(t)
        if f1==f2:
            return True
        else:
            return False