class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        last = 0
        for index, space in enumerate(spaces):
            ans += s[last:space] + " "
            last = space
        ans += s[space:]
        return ans