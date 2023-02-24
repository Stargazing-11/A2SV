class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextG = {}
        monStk = []
        
        for num in nums2:
            if not monStk:
                monStk.append(num)
            while monStk and monStk[-1] < num:
                nextG[monStk.pop()] = num
            monStk.append(num)
            
        ans = []
        for num in nums1:
            if num in nextG:
                ans.append(nextG[num])
            else:
                ans.append(-1)
        return ans