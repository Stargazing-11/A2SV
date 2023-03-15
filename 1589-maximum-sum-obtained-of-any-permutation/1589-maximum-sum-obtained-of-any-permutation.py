class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref = [[0, i] for i in range(len(nums))]
        mod = pow(10, 9) + 7
        
        for request in requests:
            pref[request[0]][0] += 1
            if request[1] + 1 < len(nums):
                pref[request[1] + 1][0] -= 1
        
        for i in range(1, len(nums)):
            pref[i][0] += pref[i-1][0]
        
        pref.sort(reverse=True)
        nums.sort(reverse=True)
        
        newArr = [0 for _ in range(len(nums))]

        for i in range(len(pref)):
            if pref[i][1] < len(nums):
                newArr[pref[i][1]] = nums[i]
                
        newPref = [0]

        for i in range(len(newArr)):
            newPref.append(newPref[-1] + newArr[i])
            
        total = 0
        
        for start, end in requests:
            total += (newPref[end+1] - newPref[start])
        return total % mod