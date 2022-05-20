class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        sum1 = count = i = 0
        x = Counter(arr)
        s = x.most_common()
        while sum1 < len(arr)//2:
            sum1+= s[i][1]
            i +=1
            count+=1
        return count