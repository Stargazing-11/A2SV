class Solution:
    def interpret(self, command: str) -> str:
        temp = ""
        output = ""
        dicts = {
            "(al)": "al",
            "()": "o"
        }
        for char in command:
            if char == "G":
                output += "G"
            elif char == ")":
                temp += char
                output += dicts[temp]
                temp = ""
            else:
                temp += char
        return output
