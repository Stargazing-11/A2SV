class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        tempScore = 0
        left, right = 0, len(tokens) - 1

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                tempScore += 1
                score = max(tempScore, score)
            elif tempScore > 0:
                power += tokens[right]
                right -= 1
                tempScore -= 1
            else:
                break
        return score
