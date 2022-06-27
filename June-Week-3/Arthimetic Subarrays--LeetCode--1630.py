class Solution:
    def check(self, arth):
        if len(arth) <= 2:
            return True
        arth.sort()
        dif = arth[1] - arth[0]
        for i in range(1,len(arth) - 1):
            if abs(arth[i+1] - arth[i]) != abs(dif):
                return False
        return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(r)):
            arth = nums[l[i]:r[i]+1]
            ans.append(self.check(arth))
        return ans