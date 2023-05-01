class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def bfs(room):
            que = deque([room])
            visited = set()
            while que:
                room = que.popleft()
                visited.add(room)
                if len(visited) == len(rooms): return True
                for key in rooms[room]:
                    if key not in visited:
                        que.append(key)
            return False
        return bfs(0)
    