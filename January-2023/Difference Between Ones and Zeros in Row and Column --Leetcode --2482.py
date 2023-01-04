class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        col = defaultdict(int)
        row = defaultdict(int)
        for index, line in enumerate(grid):
            counted = Counter(line)
            row[index] = counted[1] - counted[0]
            for ind, num in enumerate(line):
                if num == 0:
                    col[ind] += 1

        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                val = row[i] + ((len(grid) - col[j]) - col[j])
                temp.append(val)
            ans.append(temp)
        return ans
