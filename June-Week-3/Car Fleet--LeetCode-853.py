class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = []
        fleet = 0
        for i in range(len(position)):
            time = (target-position[i]) / speed[i]
            pos_time.append([position[i], time])        
        pos_time.sort()
        pos_time.reverse()
        mon_stk = []
        for i in pos_time:
            if not mon_stk:
                mon_stk.append(i)
                fleet = 1
            else:
                if mon_stk[-1][1] < i[1]:
                    mon_stk.pop()
                    mon_stk.append(i)
                    fleet += 1
        return fleet