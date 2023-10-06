class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        
        bits = [format(num, 'b') for num in nums]
        
        max_l = 0
        for bit in bits:
            max_l = max(max_l, len(bit))
            
        for i in range(len(bits)):
            dif = max_l - len(bits[i])
            new_bit = "0" * dif + bits[i]
            bits[i] = new_bit


        max_xor = 0
            
        def insert(num):
            cur = trie
            for c in num:
                if c not in cur:
                    cur[c] = {}
                
                cur = cur[c]
    
        def search(num, length):
            cur = trie
            count = 0
            for c in num:
                if c == "0":
                    if "1" in cur:
                        count += 2 ** (length - 1)
                        c = "1"
                elif c == "1":
                    if "0" in cur:
                        count += 2 ** (length - 1)
                        c = "0"
                cur = cur[c]
                length -= 1
            return count

        for bit in bits:
            insert(bit)  
        
        for bit in bits:
            max_xor = max(max_xor, search(bit, len(bit)))
            
        return max_xor
                        
                        
                    
                    
                    