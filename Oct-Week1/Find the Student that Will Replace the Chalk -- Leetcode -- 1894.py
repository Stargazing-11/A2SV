class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        prefSum =[chalk[0]]
        for i in chalk[1:]:
            prefSum.append(prefSum[-1] + i)

        k = k % prefSum[-1]
        
        if k == 0 or k < chalk[0]:
            return 0

        prefSum.reverse()

        for index, num in enumerate(prefSum):
            if k - num >= 0:
                return len(prefSum)- index