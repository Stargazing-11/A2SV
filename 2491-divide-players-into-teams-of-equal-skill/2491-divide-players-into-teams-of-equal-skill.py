class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 1, len(skill) - 2
        
        temp = skill[0] + skill[-1]
        ansSum = skill[0] * skill[-1]
        
        while left < right:
            if skill[left] + skill[right] == temp:
                ansSum += (skill[left] * skill[right])
            else:
                return -1
            right -= 1
            left += 1
        return ansSum
        