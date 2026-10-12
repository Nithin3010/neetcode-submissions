class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=list(s.split())
        match={}
        j=0
        if len(s)!=len(pattern):
            return False
        for i in pattern:
            if i in match:
                if s[j]==match[i]:
                    j+=1
                    continue
                else:
                    return False
            else:
                match[i]=s[j]
            j+=1
        if len(set(match.values()))!=len(match.values()):
            return False
        return True


        