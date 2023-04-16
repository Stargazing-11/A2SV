class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dics = {}
        
        for i, j in enumerate(s):
            if j not in dics and t[i] in dics.values():
                return False
            else:
                if j in dics and dics[j] != t[i]:
                    return False
            dics[j] = t[i]
        return True