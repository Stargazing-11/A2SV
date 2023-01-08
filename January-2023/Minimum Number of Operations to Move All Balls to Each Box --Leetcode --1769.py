class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = defaultdict(int)

        for index, box in enumerate(boxes):
            if box == "1":
                balls[index] += 1

        ans = defaultdict(int)

        for ind, box in enumerate(boxes):
            for key in balls.keys():
                ans[ind] += abs(ind - key)
            ans[ind] += 0

        return list(ans.values())
