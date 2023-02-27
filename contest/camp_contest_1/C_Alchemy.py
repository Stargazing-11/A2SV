n = int(input())
seq = list(map(int, input().split(" ")))

lSum, rSum = 0, 0
ed, al = 0, len(seq) - 1
while ed <= al:
    if lSum + seq[ed] > rSum + seq[al]:
        rSum += seq[al]
        al -= 1
    else:
        lSum += seq[ed]
        ed += 1
print(ed, n - 1 - al)