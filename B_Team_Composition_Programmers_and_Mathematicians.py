t = int(input())

def checkGroup(maths, prog, mid):
    if mid == 0:
        return True
    
    if maths // mid >= 1 and prog // mid and (maths + prog) // mid >= 4:
        return True
    return False

for _ in range(t):
    maths, prog = map(int, input().split())

    left, right = 0, min(maths, prog)

    while left <= right:
        mid = (left + right) // 2

        if checkGroup(maths, prog, mid):
            left = mid + 1
        else:
            right = mid -1 
    print(right)

    