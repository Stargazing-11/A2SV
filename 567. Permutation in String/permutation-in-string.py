class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) <  len(s1):
            return False

        
        count_s1 = defaultdict(int)
        count_s2 = defaultdict(int)
        
        for i in range(len(s1)):
            count_s1[s1[i]] += 1            
            count_s2[s2[i]] += 1
            
        if count_s1 == count_s2:
            return True
        
        l, r = 1, len(s1)
        
        while r < len(s2):
            count_s2[s2[l-1]] -= 1
            
            if count_s2[s2[l-1]] == 0:
                del count_s2[s2[l-1]]
            
            count_s2[s2[r]] += 1
            
            if count_s2 == count_s1:
                return True
            l += 1
            r += 1
        return False
        
        
        
        

        