# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
words = []
for i in range(int(input())):
    words.append(input())
counted = Counter(words)
print(len(counted))
print(*counted.values());