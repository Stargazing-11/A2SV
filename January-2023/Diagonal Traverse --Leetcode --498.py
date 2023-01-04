class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashMap = defaultdict(list)

        for index, row in enumerate(mat):
            for ind, num in enumerate(row):
                hashMap[index + ind].append(num)
        ans = []
        for key in hashMap.keys():
            if key % 2 == 0:
                hashMap[key].reverse()
            ans.extend(hashMap[key])

        return ans
