class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        avail_bills = {5 : 0, 10: 0, 20 : 0}
        
        for bil in bills:
            if bil == 10:
                if not avail_bills[5]:
                    return False        
                else:
                    avail_bills[5] -= 1
            if bil == 20:
                if avail_bills[5] and avail_bills[10]:
                    avail_bills[5] -=1 
                    avail_bills[10] -= 1
                    
                elif avail_bills[5] >= 3:
                    avail_bills[5] -= 3
                else:
                    return False
            avail_bills[bil] += 1
        return True