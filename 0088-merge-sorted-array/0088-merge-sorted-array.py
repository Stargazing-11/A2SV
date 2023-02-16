class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        one, two, right = m-1, n-1, n+m - 1
        
        while two >= 0:
            
            if one >= 0 and nums1[one] >= nums2[two]:
                nums1[right] = nums1[one]
                nums1[one] = 0
                one -= 1
            else: 
                nums1[right] = nums2[two]
                two -= 1
            right -= 1
            # print(nums1)