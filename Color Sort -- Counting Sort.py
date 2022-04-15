class Solution:
    def sortColors(self, nums: List[int]) -> None:
        x = 0 
        y=0
        z=0
        for i in range(len(nums)):
            if nums[i] == 0:
                x+=1
            elif nums[i] == 1:
                y +=1
            else:
                z +=1
        print(x,y,z)
        for j in range(x):
            nums[j] = 0
        print(nums)
        for k in range(x, x + y):
            nums[k] = 1
        print(nums)
        for l in range(x + y, len(nums)):
            nums[l] = 2
        print(nums)