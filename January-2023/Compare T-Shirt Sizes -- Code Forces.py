
t = int(input())
for test in range(t):
    tshirts = input().split()
    a, b = tshirts[0], tshirts[1]
    a = a[::-1]
    b = b[::-1]
    cond = False
    for i in range (min(len(a), len(b))):
        if ord(a[i]) < ord(b[i]):
            print(">")
            cond = True
            break
        elif ord(a[i]) > ord(b[i]):
            print("<")
            cond = True
            break
    if i + 1 < len(a) and cond == False:
        if a[0] == "L":
            print(">")
        else:
            print("<")
    elif i + 1 < len(b) and cond == False:
        if a[0] == "L":
            print("<")
        else:
            print(">")
    elif i + 1 >= len(a) and i + 1 >= len(b) and cond == False:
        print("=")