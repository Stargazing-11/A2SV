class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        mon_que = deque()
        ans = len(nums) + 1
        pref_sum = [0]
        
        for num in nums:
            pref_sum.append(pref_sum[-1] + num)

        for i in range(len(pref_sum)):
            while mon_que and pref_sum[i] - pref_sum[mon_que[0]] >= k:
                ans = min(ans, i - mon_que.popleft())
            while mon_que and pref_sum[mon_que[-1]] > pref_sum[i]:
                mon_que.pop()
            mon_que.append(i)
        return ans if ans <= len(nums) else -1 