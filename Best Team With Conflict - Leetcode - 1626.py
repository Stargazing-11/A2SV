class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        ageScore = sorted(list(zip(ages, scores)))
        # ageScore.sort(key = lambda x: (x[0], x[1]))
        # @cache
        # def dp(i):
        #     if i == 0:
        #         return ageScore[i][1]

        #     maxVal = 0

        #     for j in range(i):
        #         if ageScore[j][1] <= ageScore[i][1]:
        #             maxVal = max(maxVal, dp(j))
        #     return maxVal + ageScore[i][1]
        
        # return max(dp(i) for i in range(len(scores)))

        dp = [ageScore[i][1] for i in range(n)]

        for i, (_, score) in enumerate(ageScore):
            for j in range(i):
                if ageScore[j][1] <= score:
                    dp[i] = max(dp[i], score + dp[j])

        return max(dp)
