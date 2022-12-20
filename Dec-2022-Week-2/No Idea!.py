# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
n = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(sum([1 if c in a else -1 if c in b else 0 for c in n]))
