class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitsCount = {fruits[0]:1}
        fruitsInBasket = set()
        fruitsInBasket.add(fruits[0])
        maxFruits = 0
        left, right = 0, 1
        
        while right < len(fruits):
            while len(fruitsInBasket) == 2 and fruits[right] not in fruitsInBasket:
                maxFruits = max(maxFruits, right - left)
                fruitsCount[fruits[left]] -= 1
                if fruitsCount[fruits[left]] == 0:
                    del fruitsCount[fruits[left]]
                    fruitsInBasket.remove(fruits[left])
                left+=1
            
            fruitsInBasket.add(fruits[right])
            
            if fruits[right] in fruitsCount:
                fruitsCount[fruits[right]] += 1
            else:
                fruitsCount[fruits[right]] = 1
            right += 1
        return max(maxFruits, right - left)