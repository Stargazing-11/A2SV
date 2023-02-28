class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trip_range = [0 for i in range(1001)]
        
        for trip in trips:
            trip_range[trip[1]] += trip[0]
            trip_range[trip[2]] -= trip[0]
        
        for i in range(0, len(trip_range)):
            add = trip_range[i-1] if i > 0 else 0
            trip_range[i] += add 

            if trip_range[i] > capacity:
                return False
        return True