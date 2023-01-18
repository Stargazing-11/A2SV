class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        counted = defaultdict(int)
        n = len(nums)

        for i in range(n):
            counted[nums[i]] += 1
            temp = int(str(nums[i])[::-1])
            counted[temp] += 1
            nums.append(temp)
        return len(counted.keys())
