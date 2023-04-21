class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcf(a, b):
            if b == 0:
                return a
            return gcf(b, a%b)
        
        counted = Counter(deck)
        keys = list(counted.keys())
        cur_gcf = counted[keys[0]]
        
        for key in keys[1:]:
            cur_gcf = gcf(cur_gcf, counted[key])
        
        if cur_gcf > 1:
            return True
        return False