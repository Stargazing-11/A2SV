class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        change = []
        
        min_cost = 0
        
        for citya, cityb in costs:
            min_cost += citya
            
            change.append(cityb - citya)
        
        change.sort()
        
        for i in range(len(costs)//2):
            min_cost += change[i]
            
        return min_cost