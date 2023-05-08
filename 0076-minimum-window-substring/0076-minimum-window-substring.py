class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cur_count = defaultdict(int)
        counted = Counter(t)
        t = set(t)
        
        need = len(t)
        left, cur_have, min_window = 0, 0, [float("-inf"), float("inf")]

        for right in range(len(s)):
            if s[right] in t:
                cur_count[s[right]] += 1
            
            if s[right] in t and cur_count[s[right]] == counted[s[right]]:
                cur_have += 1
 
            while cur_have == need:
                if min_window[1] - min_window[0] > right - left:
                    min_window = [left, right]
                if s[left] in t:
                    cur_count[s[left]] -= 1
                    if cur_count[s[left]] < counted[s[left]]:
                        cur_have -= 1
                left += 1

        return s[min_window[0]:min_window[1] + 1] if min_window[0] != float("-inf") else ""