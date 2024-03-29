class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThan = []
        equal = []
        greaterThan = []

        for num in nums:
            if num < pivot:
                lessThan.append(num)
            elif num > pivot:
                greaterThan.append(num)
            else:
                equal.append(num)
        ans = lessThan + equal + greaterThan
        return ans
