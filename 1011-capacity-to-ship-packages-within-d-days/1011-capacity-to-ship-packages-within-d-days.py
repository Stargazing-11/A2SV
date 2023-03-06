class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkCapacity(capacity):
            load = 0
            day = 1
            
            for weight in weights:
                load += weight
                if load > capacity:
                    day += 1
                    load = weight
            if day <= days:
                return True
            return False
        
        left, right = max(weights), sum(weights)
        
        while left <= right:
            mid = (left + right) // 2
            if checkCapacity(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left