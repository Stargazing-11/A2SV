class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        deadends = set(deadends)
        
        def get_neighbors(lock):
            neighbors = []
            
            for i in range(len(lock)):
                back = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:]
                front = lock[:i] + str((int(lock[i]) - 1) % 10) + lock[i+1:]
                neighbors.append(back)
                neighbors.append(front) 
            return neighbors
        
        visited = {"0000"}
        que = deque([("0000", 0)])
        
        while que:
            
            lock, turn = que.popleft()
            if lock == target:
                return turn
            
            neighbors = get_neighbors(lock)
            
            for neighbor in neighbors:
                if neighbor not in deadends and neighbor not in visited:
                    visited.add(neighbor)
                    que.append((neighbor, turn + 1))

        return -1 