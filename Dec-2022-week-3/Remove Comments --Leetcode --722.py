class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        block = False
        buffer = ""

        for line in source:
            index = 0

            while index < len(line):
                char = line[index]

                if char == "/" and index + 1 < len(line) and line[index + 1] == "/" and block == False:
                    index = len(line)
                elif char == "/" and index + 1 < len(line) and line[index + 1] == "*" and block == False:
                    block = True
                    index += 1
                elif char == "*" and index + 1 < len(line) and line[index + 1] == "/" and block:
                    block = False
                    index += 1
                elif not block:
                    buffer += char
                index += 1

            if buffer and not block:
                answer.append(buffer)
                buffer = ""
        return answer
