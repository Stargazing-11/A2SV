t = int(input())

for _ in range(t):
    x = int(input())    
    if x == 1:
        print(3)
    elif x % 2 != 0:
        print(1)
    else:
        # while n 
        c = 0
        y = 2
        while (x & pow(y, c)) == 0:
            c += 1
        if pow(y, c) == x:
            print(pow(y, c) + 1)
        else:
            print(pow(y, c))