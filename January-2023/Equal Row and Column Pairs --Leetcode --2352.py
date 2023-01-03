class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = defaultdict()
        col = defaultdict(list)

        for ind, line in enumerate(grid):
            row[ind] = line

            for index, num in enumerate(line):
                col[index].append(num)

        count = 0
        for key in row.keys():
            for key2 in col.keys():
                if row[key] == col[key2]:
                    count += 1
        return count