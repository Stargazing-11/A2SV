class RandomizedSet:

    def __init__(self):
        self.randomSet = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val not in self.randomSet:
            self.randomSet[val] = len(self.vals)
            self.vals.append(val)
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            index = self.randomSet[val]
            end = self.vals[-1]

            self.vals[index] = end
            self.randomSet[end] = index
            
            self.vals.pop()
            del self.randomSet[val]

            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()