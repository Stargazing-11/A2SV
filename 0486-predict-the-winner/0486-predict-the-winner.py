class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        player1 = 0
        player2 = 0
        
        def predict(left, right, player1, player2, turn):
            if left > right:
                return player1 >= player2 
            if turn:
                p1c1 = predict(left+1, right, player1 + nums[left], player2, 1-turn)
                p1c2 = predict(left, right - 1, player1 + nums[right], player2, 1-turn)
                return p1c1 or p1c2
            else:
                p2c1 = predict(left+1, right, player1, player2 + nums[left], 1-turn)
                p2c2 = predict(left, right - 1, player1, player2 + nums[right], 1-turn)
                return p2c1 and p2c2
        return predict(0, len(nums)-1, player1, player2, 1)