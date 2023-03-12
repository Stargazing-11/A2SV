class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output = [0 for i in range(n + 1)]
        
        
        for booking in bookings:
            output[booking[0]-1] += booking[2]
            output[booking[1]] -= booking[2]
            
        for i in range(1, len(output)):
            output[i] += output[i-1]
            
        return output[:-1]