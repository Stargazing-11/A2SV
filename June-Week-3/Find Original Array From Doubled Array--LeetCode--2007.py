from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 >0:
            return []
        changed.sort()
        counted = Counter(changed)
        original = []
        z = counted[0] // 2
        
        for i in changed:
            if i == 0 and counted[i] >= 2:
                counted[i] -= 2
                original.append(i)
            elif i > 0 and counted[i] and counted[i*2]:
                counted[i] -= 1
                counted[i*2] -= 1
                original.append(i)
        res = original if len(original) == len(changed) // 2 else []
        print(original, len(changed)//2)
        return res
        