class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valids = [0, 0, float(inf), -1]

        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                point.append(abs(x - point[0]) + abs(y - point[1]))
                point.append(index)
                if valids[2] > point[2]:
                    valids = point
                elif valids[2] == point[2]:
                    valids = valids if valids[0] <= point[0] or valids[1] <= point[1] else point
        print(valids)
        return valids[-1] if valids[2] != float(inf) else -1
