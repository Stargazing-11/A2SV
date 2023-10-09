class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        lps = [0]*len(needle)
        prei, curi = 0, 1
        
        while curi < len(needle):
            if needle[prei] == needle[curi]:
                lps[curi] = prei + 1
                prei += 1
                curi += 1
            
            elif prei == 0:
                curi += 1
                
            else:
                prei = lps[prei - 1]
        
        s_i, n_i = 0, 0
        
        while s_i < len(haystack):
            if needle[n_i] == haystack[s_i]:
                s_i += 1
                n_i += 1
            
            elif n_i == 0:
                s_i += 1
            
            else:
                n_i = lps[n_i - 1]
            
            if n_i == len(needle):
                return s_i - n_i
        return -1