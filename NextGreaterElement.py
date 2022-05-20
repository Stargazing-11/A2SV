class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in nums1:
            x = nums2.index(i)
            print(x)
            l = 0
            for j in range(x+1, len(nums2)):
                if x + 1 < len(nums2):
                    if nums2[j] > i:
                        print(j)
                        output.append(nums2[j])
                        print(output)
                        l = 1
                        break
            if l == 0:
                output.append(-1)
        return output  