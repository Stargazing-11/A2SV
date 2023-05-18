class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        min_heap = []
        heapify(min_heap)
        heappush(min_heap, (nums1[0]+nums2[0], 0, 0))
        
        ans = []
        
        visited = {(0, 0)}
        while min_heap and len(ans) < k:
            
            prev_sum, i, j = heappop(min_heap)
            visited.add((i, j))
            
            ans.append([nums1[i], nums2[j]])
            
            if (i+1, j) not in visited and i+1 < len(nums1):
                heappush(min_heap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
                
            if (i, j+1) not in visited and j+1 < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))
                
        return ans