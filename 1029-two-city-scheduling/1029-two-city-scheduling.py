class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        difference = [cost[1] - cost[0] for cost in costs]
        total_cost = sum([cost[0] for cost in costs])
        
        difference.sort()
        total_cost += sum(difference[:(len(difference)//2)])
        
        return total_cost