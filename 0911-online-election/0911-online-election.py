class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        
        count = defaultdict(int)
        count[persons[0]] = 1
        self.mostelected = [persons[0]]
        big = [persons[0], 1]
        
        for person in persons[1:]:
            count[person] += 1
            if big[1] == count[person] or count[person] > big[1]:
                big = [person, count[person]]
            self.mostelected.append(big[0])
            
    def q(self, t: int) -> int:
        
        left, right = 0, len(self.times)-1
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.times[mid] < t:
                left = mid + 1
            elif self.times[mid] > t:
                right = mid - 1
                
            else:
                left = mid + 1
                break
            
        return self.mostelected[left-1]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)