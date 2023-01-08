class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numdict = defaultdict(int)

        for index, num in enumerate(nums):
            numdict[num] = index

        for opr in operations:
            temp = numdict[opr[0]]
            del numdict[opr[0]]
            numdict[opr[1]] = temp

        for key in numdict.keys():
            nums[numdict[key]] = key
        return nums
