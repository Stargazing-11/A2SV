class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        count = 0
        while tickets[k] > 0:
            if tickets[count%len(tickets)] > 0:
                tickets[count%len(tickets)] -= 1
                time += 1
            count += 1
        return time
            