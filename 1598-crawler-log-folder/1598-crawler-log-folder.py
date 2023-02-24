class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for log in logs:
            if log[0].isalnum():
                stk.append(log)
            elif log == "../" and stk:
                stk.pop()
        return len(stk)
    