class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero = {}
        one = {}
        ans = [[], []]
        for match in matches:
            left, right = match[0], match[1]
            if left not in zero:
                if left not in one:
                    zero[left] = 1
            if right not in one:
                if right in zero:
                    del zero[right]
                one[right] = 1
            elif right in one:
                one[right] += 1

        for key in zero.keys():
            ans[0].append(key)
        ans[0].sort()
        for key in one.keys():
            if one[key] <= 1:
                ans[1].append(key)
        ans[1].sort()
        return ans
