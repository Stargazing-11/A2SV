class Solution:
    def largestNumber(self, nums: List[int]) -> str: 

        def func(x, y):
            if x + y > y+x:
                return 1
            elif y+x > x+y:
                return -1
            else:
                return 0
        nums = sorted([str(num) for num in nums], key=cmp_to_key(func), reverse = True)
        return str(int("".join(nums)))