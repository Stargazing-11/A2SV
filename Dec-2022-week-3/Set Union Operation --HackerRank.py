# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english = set(input().split(" "))
m = int(input())
french = set(input().split(" "))
print(len(english.union(french)))