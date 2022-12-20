class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for char in s:
            if char.isalnum():
                if 65 <= ord(char) <= 90:
                    newStr += chr(ord(char) + 32)
                else:
                    newStr += char
        return newStr == newStr[::-1]