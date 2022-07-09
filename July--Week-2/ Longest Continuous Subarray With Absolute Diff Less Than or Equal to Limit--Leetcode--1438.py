    class Solution:
        def longestSubarray(self, nums: List[int], limit: int) -> int:
            monque = [nums[0]]
            maxN = monque[0]
            minN = monque[0]
            ans = 1
            for i in range(1, len(nums)):
                new = nums[i]
                monque.append(new)

                if new > maxN:
                    maxN = new
                elif new < minN:
                    minN = new
                if new>maxN:
                    maxN=new
                if new < minN:
                    minN=new

                if maxN-minN <= limit:
                    ans = max(ans, len(monque))
                else:
                    monque.pop(0)
                    while max(monque)- min(monque) > limit:
                        if len(monque) > 3000:
                            return ans
                        monque.pop(0)
                    maxN = max(monque)
                    minN = min(monque)
            return ans

                    