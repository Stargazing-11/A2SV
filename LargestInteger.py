class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        z = []
        d = 0
        for k in range(len(nums)):
            if nums[k] !=0:
                z.append(nums[k])
            nums[k] = str(nums[k])
        for i in range(len(z)):
            if z[i] !=0:
                d += 1
                break
        if d == 0:
            return "0"
        for i in range(len(nums)):
            minL = i
            for j in range (i,len(nums)):
                x = len(nums[j])
                y = len(nums[minL])
                for l in range(min(x,y)):
                    if (int(nums[j][l]) > int(nums[minL][l])):
                        minL = j
                        break
                    elif int(nums[minL][l]) > int(nums[j][l]):
                        break
                    else:
                        if int(nums[j] + nums[minL]) > int(nums[minL] + nums[j]):
                            minL = j
            nums[minL], nums[i] = nums[i], nums[minL]
            
        nums = "".join(nums)
        return nums