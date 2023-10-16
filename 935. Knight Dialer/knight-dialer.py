class Solution:
    def knightDialer(self, n: int) -> int:
        jumps = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]

        cache = {}
        def dp(jumps_left, square):
            if jumps_left == 0:
                return 1
            
            state = (jumps_left, square)
            if state in cache:
                return cache[state]
            
            temp = 0
            for next_square in jumps[square]:
                temp += dp(jumps_left - 1, next_square)
                
            cache[state] = temp
            return cache[state]
        
        ans = 0
        for i in range(10):
            ans += dp(n-1, i)
        return ans % (10 ** 9 + 7)