class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        def checkK(k):
            hr, carry = 0, 0
            for pile in piles:
                hr += math.ceil(pile/k)
                
            if hr <= h:
                return True
            return False
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if checkK(mid):
                right = mid 
            else:
                left = mid + 1
        return left if checkK(left) else right