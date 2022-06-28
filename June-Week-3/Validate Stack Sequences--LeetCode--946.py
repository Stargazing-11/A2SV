class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        counter = 0
        for i, val in enumerate(pushed):
            stack.append(val)
            while stack and stack[-1] == popped[counter] and counter < len(popped):
                stack.pop()
                counter += 1
        return stack == [] 