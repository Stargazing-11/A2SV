class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
#         cache = {}
        
#         def dp(i, j):
            
#             if i >= len(nums1) or j >= len(nums2):
#                 return 0
            
#             if (i,j) in cache:
#                 return cache[(i, j)]

#             if nums1[i] == nums2[j]:
#                 max_lines = 1 + dp(i+1, j+1)
            
#             else:
#                 max_lines = max(dp(i+1, j), dp(i, j+1))
            
#             cache[(i,j)] = max_lines
#             return cache[(i,j)]
        
#         return dp(0, 0)
    
        n, m = len(nums1) + 1, len(nums2) + 1
        dp = [[0] * m for i in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[n-1][m-1]
    