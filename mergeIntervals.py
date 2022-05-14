class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(intervals)
        k = 1
        output = [intervals[0]]
        # cur = intervals[0]
        while k < len(intervals):
            # print(intervals[k][0], cur[1])
            if intervals[k][0] <= output[-1][1]:
                # cur = [cur[0], max(cur[1], intervals[k][1])]
                output[-1][1] = max(output[-1][1], intervals[k][1])
            else:
                output.append(intervals[k])
                # cur = intervals[k]
            k += 1
        return output