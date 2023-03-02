class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        posAndTime = []
        mon_stk = []
        for i in range(len(position)):
            posAndTime.append([position[i], (target-position[i])/speed[i]])
        
        posAndTime.sort(reverse=True)

        for i in range(len(posAndTime)):
            if not mon_stk:
                mon_stk.append(posAndTime[i][1])
                ans = 1
            else:
                if mon_stk[-1] < posAndTime[i][1]:
                    mon_stk.pop()
                    mon_stk.append(posAndTime[i][1])
                    ans += 1
        return ans