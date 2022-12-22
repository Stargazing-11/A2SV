class Solution:
    def countPairs(self, ds: List[int]) -> int:
        dct = defaultdict(int)

        ans = 0

        for delc in ds:
            for i in range(22):
                ans += dct[2 ** i - delc]
            dct[delc] += 1

        return ans % 1000000007
