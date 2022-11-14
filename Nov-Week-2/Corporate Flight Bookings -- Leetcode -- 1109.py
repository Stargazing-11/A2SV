class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+1)
        for book in bookings:
            diff[book[0]-1] += book[2]
            diff[book[1]] -= book[2]
        prefSum = 0
        for j in range(len(diff)):
            prefSum += diff[j]
            diff[j] = prefSum
        return diff[:n]
