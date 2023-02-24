class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextG = defaultdict(lambda: -1)
        monStk = []
        
        for num in nums2:
            if not monStk:
                monStk.append(num)
            while monStk and monStk[-1] < num:
                nextG[monStk.pop()] = num
            monStk.append(num)
            
        return [nextG[num] for num in nums1]