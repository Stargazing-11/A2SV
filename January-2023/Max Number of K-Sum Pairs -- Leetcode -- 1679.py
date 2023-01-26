class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # hash map solution
        def hashmapSolution():
            hashmap = {}
            count = 0
            for num in nums:
                if k - num in hashmap and hashmap[k-num] > 0:
                    count += 1
                    hashmap[k-num] -= 1
                else:
                    if num in hashmap:
                        hashmap[num] += 1
                    else:
                        hashmap[num] = 1
            return count
        # Two Pointer approach

        def twoPointerandSortingSolution():
            nums.sort()
            left, right = 0, len(nums)-1
            count = 0
            while left < right:
                if nums[left] + nums[right] > k:
                    right -= 1
                elif nums[left] + nums[right] < k:
                    left += 1
                else:
                    count += 1
                    left += 1
                    right -= 1
            return count
