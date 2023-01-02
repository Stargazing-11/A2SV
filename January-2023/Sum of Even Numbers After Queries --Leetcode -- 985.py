class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        evenSum = 0
        evens = defaultdict(list)
        for index, num in enumerate(nums):
            if num % 2 == 0:
                evens["even"] = index
                evenSum += num

        for querie in queries:
            if nums[querie[1]] % 2 == 0:
                evenSum -= nums[querie[1]]
                nums[querie[1]] += querie[0]
                if nums[querie[1]] % 2 == 0:
                    evenSum += nums[querie[1]]
                ans.append(evenSum)
            else:
                nums[querie[1]] += querie[0]
                if nums[querie[1]] % 2 == 0:
                    evenSum += nums[querie[1]]
                ans.append(evenSum)
        return ans
