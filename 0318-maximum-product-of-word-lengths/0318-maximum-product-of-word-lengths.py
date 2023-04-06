class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        bits = []
        
        for word in words:
            bit = 0
            for char in set(word):
                bit += (1 << (ord(char) - ord("a")))
            bits.append(bit)
            
        max_prod = 0
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if not bits[i] & bits[j]:
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
                                
        return max_prod