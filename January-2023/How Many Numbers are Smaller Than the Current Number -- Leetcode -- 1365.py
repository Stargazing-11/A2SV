class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        temp = sorted(nums.copy())
        for index, num in enumerate(temp):
            if index == 0:
                continue
            if temp[index - 1] != num:
                counter[num] += index

        ans = []

        for num in nums:
            ans.append(counter[num])
        return ans
