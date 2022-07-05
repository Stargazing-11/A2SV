import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        newnums = nums.copy()
        total = []
        for j,i in enumerate(newnums):
            if not total:
                newnums.pop(j)
                total.append(math.prod(newnums))
                newnums.insert(j, i)
            else:
                if i == 0:
                    z = Counter(nums)
                    if z[0] == 1:
                        newnums.pop(j)
                        total.append(math.prod(newnums))
                        newnums.insert(j, i)
                        continue
                    else:
                        newt = (total[j-1] * nums[j-1])
                else:
                    newt = (total[j-1] * nums[j-1]) // i
                total.append(newt)
        return total