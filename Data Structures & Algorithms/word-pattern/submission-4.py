class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        match={}
        if len(s)!=len(pattern):
            return False
        for j,i in enumerate(pattern):
            if i in match:
                if s[j]==match[i]:
                    continue
                else:
                    return False
            else:
                match[i]=s[j]
        if len(set(match.values()))!=len(match):
            return False
        return True


        