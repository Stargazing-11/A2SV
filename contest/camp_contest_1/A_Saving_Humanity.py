tests = int(input())
for _ in range(tests):
    n, m = map(int, input().split())
    
    soliders = list(input())
    
    near1Left = float("-inf")
    near1Right = float("inf")
    
    left = []
    right = []
    
    for i in range(1, len(soliders)+1):
        left.append(near1Left)
        right.append(near1Right)
        if int(soliders[i-1]) == 1:
            near1Left = i-1
        
        if int(soliders[-i]) == 1:
            near1Right = len(soliders) - i

    right.reverse()
    ans = []
    for i in range(len(soliders)):
        if int(soliders[i]) == 1:
            ans.append("1")
        else:
            if abs(left[i] - i) != abs(right[i] - i) and min(abs(left[i] - i), abs(right[i] - i)) <= m:
                ans.append("1")
            else:
                ans.append("0")
    print("".join(ans))
                
    