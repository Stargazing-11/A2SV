class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return (sum(salary) - salary[-1] - salary[0]) / (len(salary) - 2)
