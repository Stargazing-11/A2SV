class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def backtrack(start, curr):
            if start >= len(num):
                if len(curr) > 2 and int(num[curr[-3][0]:curr[-3][1]]) + int(num[curr[-2][0]:curr[-2][1]]) == int(num[curr[-1][0]:curr[-1][1]]):
                    return True
                return False
            for index in range(start, len(num)):
                ans = False
                if int(num[curr[-1][0]:curr[-1][1]]) + int(num[curr[-2][0]:curr[-2][1]]) == int(num[curr[-1][1]:index+1]):
                    if len(num[curr[-1][1]:index+1]) > 1 and num[curr[-1][1]:index+1][0] == "0":
                        break
                    curr.append((curr[-1][1], index+1))
                    ans = backtrack(index + 1, curr)
                    curr.pop()
                    if ans:
                        return True
                elif int(num[curr[-1][0]:curr[-1][1]]) + int(num[curr[-2][0]:curr[-2][1]]) < int(num[curr[-1][1]:index+1]):
                    break
            return False
        
        for index in range(len(num)):
            if len(num[0:index+1]) > 1 and num[0:index+1][0] == "0":
                    break
            curr = [(0, index+1)]
            for ind in range(index+1, len(num)):
                if len(num[index+1:ind+1]) > 1 and num[index+1:ind+1][0] == "0":
                    break
                curr.append((index+1, ind+1))
                ans = backtrack(ind + 1, curr)
                curr.pop()
                if ans:
                    return True
        return False