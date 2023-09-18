class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i, task in enumerate(tasks):
            task.append(i)
            
        tasks.sort()
        ans, minHeap = [], []
        
        time, i = tasks[0][0], 0
        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            if minHeap:
                processTime, index = heapq.heappop(minHeap)
                time += processTime
                ans.append(index)
            else:
                time = tasks[i][0]
            
        return ans