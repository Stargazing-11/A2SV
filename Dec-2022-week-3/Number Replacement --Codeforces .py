from collections import *


t = int(input())

for i in range(t):
    n = int(input())
    dic = defaultdict(list)
    arr = list(map(int, input().split()))
    string = list(input())
    flag = False

    for (num, char) in zip(arr, string):
        value = dic[num]
        if len(value) > 0:
            if value[-1] != char:
                print('NO')
                flag = True
                break
            else:
                dic[num].append(char)
        else:
            dic[num].append(char)

    if flag == False:
        print('YES')
