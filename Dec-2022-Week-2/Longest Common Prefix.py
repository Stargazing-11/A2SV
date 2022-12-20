class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans = strs[0]
        
        for i in range(1, len(strs)):
            test = strs[i]
            temp = []
            for i in range(min(len(test), len(ans))):
                if test[i] == ans[i]:
                    temp.append(ans[i])
                else:
                    break
            ans = temp
        ans = "".join(ans)
        return ans