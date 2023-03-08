class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = [-1 for i in range(len(intervals))]
        intervals_dict = {float(inf):-1}
        for i, interval in enumerate(intervals):
            intervals_dict[interval[0]] = i

        intervals.sort()

        def getRight(interval, i):
            left, right = i, len(intervals) - 1
            res = float(inf)
            
            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][0] >= interval[1]:
                    res = intervals[mid][0]
                    right = mid - 1
                else:
                    left = mid + 1
            return res
        
        for i, interval in enumerate(intervals):
            res = getRight(interval, i)
            ans[intervals_dict[interval[0]]] = intervals_dict[res]
        return ans 