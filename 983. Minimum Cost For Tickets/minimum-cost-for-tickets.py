class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        cache = {}
        lastDay = max(days)
        daysSet = set(days)
        
        def dp(curDay):
            if curDay > lastDay:
                return 0
            
            if curDay in cache:
                return cache[curDay]
            
            if curDay not in daysSet:
                return dp(curDay + 1)
           
            one = dp(curDay + 1) + costs[0]
            seven = dp(curDay + 7) + costs[1]
            thirty = dp(curDay + 30) + costs[2]
            
            cache[curDay] = min(one, seven, thirty)
            return cache[curDay]
        
        return dp(1)