class Solution:
    def freqAlphabets(self, s: str) -> str:
        temp = ""
        output = ""
        for char in s:
            if char == "#":
                while int(temp) > 26:
                    output += chr(96 + int(temp[0]))
                    temp = temp[1:]
                output += chr(96 + int(temp))
                temp = ""
            else:
                temp += char
        for j in temp:
            output += chr(96 + int(j))
        return output