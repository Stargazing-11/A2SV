class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = defaultdict(list)

        for string in strs:
            for i,s in enumerate(string):
                ans[i].append(s)
        count = 0
        for key in ans:
            if ans[key] != sorted(ans[key]):
                count += 1
        return count