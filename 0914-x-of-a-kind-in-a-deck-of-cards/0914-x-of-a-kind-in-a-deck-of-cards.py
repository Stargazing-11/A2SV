class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        def gcf(a, b):
            if b == 0:
                return a
            return gcf(b, a%b)
        
        counted = Counter(deck)
        
        cur_gcf = counted[counted[0]]
        for key in counted:
            cur_gcf = gcf(cur_gcf, counted[key])
        
        return cur_gcf > 1