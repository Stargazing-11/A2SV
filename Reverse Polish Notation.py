class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        oprators = ["+", "-", "*", "/"]
        
        nums = []
        
        for i in tokens:
            if i not in oprators:
                nums.append(i)
            else:
                x = int(nums.pop())
                y = int(nums.pop())
                
                if i == "+":
                    nums.append(y + x)
                elif i == "-":
                    nums.append(y - x)
                elif i == "*":
                    nums.append(y * x)
                elif i == "/":
                    nums.append(y / x)
        return int(nums[0])