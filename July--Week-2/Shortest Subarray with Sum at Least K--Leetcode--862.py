class Solution:
    def shortestSubarray(self, A, K):

        dp = [0] * (len(A) + 1)

        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + A[i - 1]

        res = len(A) + 1
        #
        Q = collections.deque()

        for i in range(len(dp)):
            while Q and dp[i] - dp[Q[0]] >= K:
                res = min(res, i - Q.popleft())
            while Q and dp[i] < dp[Q[-1]]:
                Q.pop() # pop right
            Q.append(i)

        return res if res != len(A)+1 else -1