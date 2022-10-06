class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        left, right = 1, len(cardPoints) - k
        
        rightSum = sum(cardPoints[right:])
        answer = rightSum

        while right < len(cardPoints):
            rightSum = rightSum - cardPoints[right] + cardPoints[left-1]
            answer= max(answer, rightSum)
            left += 1
            right += 1
        return answer
            