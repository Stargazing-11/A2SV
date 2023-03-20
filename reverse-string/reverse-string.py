class Solution:
    def reverseString(self, s: List[str], count = 1) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if count >= len(s) // 2 + 1:
            return 
        s[count-1], s[-count] = s[-count], s[count-1]
        count += 1
        self.reverseString(s, count)