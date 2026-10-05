class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1=''
        for i in s:
            if i.isalnum():
                s1+=i
        r=s1[::-1]
        if r==s1:
            return True
        return False