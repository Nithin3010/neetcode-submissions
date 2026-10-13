class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        s=s.lower()
        while l<r:
            if s[l].isalnum():
                if s[r].isalnum():   
                    if s[l]==s[r]:
                        l+=1
                        r-=1
                        continue
                    return False
                else:
                    r-=1
            else:
                l+=1
        return True
        