class Solution:
    def racecar(self, target: int) -> int:
        
        def checkReverse(pos, spped):
            if pos + speed > target and speed > 0:
                return (pos, -1)
            
            if pos + speed < target and speed < 0:
                return (pos, 1)
            
            return None
        
        que = deque([])
        que.append((0, 1, 0))
        
        visited = {(0, 1)}
        
        while que:
            pos, speed, distance = que.popleft()
            if pos == target:
                return distance

            if (pos + speed, speed * 2) not in visited:
                que.append((pos + speed, speed * 2, distance + 1))
                
            result = checkReverse(pos, speed)
            if result != None and (result[0], result[1]) not in visited:
                que.append((result[0], result[1], distance + 1))
                
                