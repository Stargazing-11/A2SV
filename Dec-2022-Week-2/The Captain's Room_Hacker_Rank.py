# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

_ = input()
print(Counter(input().strip().split()).most_common()[-1][0])
