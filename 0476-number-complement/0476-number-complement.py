class Solution:
    def findComplement(self, num: int) -> int:
        ones = pow(2, (len(bin(num)) - 2)) - 1
        
        return num ^ ones