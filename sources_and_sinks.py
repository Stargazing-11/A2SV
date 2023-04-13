n = int(input())
matrix = []
src, sink = [], []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(n):
    if sum(matrix[i]) == 0:
        sink.append(str(i+1))
    if sum([row[i] for row in matrix]) == 0:
        src.append(str(i+1))

print(len(src), " ".join(src))
print(len(sink), " ".join(sink))
