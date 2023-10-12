class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = {
            "L" : (-1, 0),
            "R" : (1, 0),
            "U" : (0, 1),
            "D" : (0, -1)
        }
        
        cur = "U"
        pos = [0, 0]
        
        for i in instructions:
            if i == "G":
                pos[0] += dirs[cur][0]                
                pos[1] += dirs[cur][1]
                
            else:
                if cur == "L":
                    if i == "R":
                        cur = "U"
                    else:
                        cur = "D"
                elif cur == "R":
                    if i == "L":
                        cur = "U"
                    else:
                        cur = "D"
                elif cur == "D":
                    if i == "L":
                        cur = "R"
                    else:
                        cur = "L"
                else:
                    cur = i
        return pos == [0, 0] or cur != "U"