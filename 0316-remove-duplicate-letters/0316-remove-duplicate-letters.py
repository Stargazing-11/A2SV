class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counted = Counter(s)
        seens = set()
        
        mon_stk = []
        
        for char in s:
            while mon_stk and (ord(mon_stk[-1]) > ord(char) and counted[mon_stk[-1]] >= 1 and char not in seens) :
                removed = mon_stk.pop()
                seens.remove(removed)
            if char not in seens:
                seens.add(char)
                mon_stk.append(char)
            counted[char] -= 1
        return "".join(mon_stk)