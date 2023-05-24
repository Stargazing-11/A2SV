class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        refunds = [cost[1] - cost[0] for cost in costs]
        total_cost = sum([cost[0] for cost in costs])
        
        refunds.sort()
        total_cost += sum(refunds[:(len(refunds)//2)])
        
        return total_cost