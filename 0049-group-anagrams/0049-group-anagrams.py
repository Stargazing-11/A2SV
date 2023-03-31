class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashTable = {}
        arr = []
        answer = []
        for index, string in enumerate(strs):
            res = ''.join(sorted(string))
            if res in hashTable:
                hashTable[res].append(index)
            else:
                hashTable[res] = [index]
                arr.append(res)
        
        for ar in arr:
            new = []
            for index in hashTable[ar]:
                new.append(strs[index])
            answer.append(new)
        return answer