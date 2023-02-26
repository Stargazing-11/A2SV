class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ranges = [0 for i in range(len(s) + 1)]
        
        for shift in shifts:
            ranges[shift[0]] += 1 if shift[2] == 1 else -1
            ranges[shift[1] + 1] += 1 if shift[2] == 0 else -1
            
        pref_sum = [ranges[0]]
        
        for i in range(1, len(ranges)):
            pref_sum.append(pref_sum[i-1] + ranges[i])
        
        ans = []
        for index, char in enumerate(s):
            new = ((ord(char) - 97 + pref_sum[index]) % 26) + 97
            ans.append(chr(new))
        return "".join(ans)