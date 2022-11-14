class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sumDict = {-1: 0}
        diff = [0] * len(trips)

        for i in trips:
            for j in range(i[1], i[2]):
                if j in sumDict:
                    sumDict[j] += i[0]
                else:
                    sumDict[j] = i[0]
                if sumDict[j] > capacity:
                    return False
        return True
