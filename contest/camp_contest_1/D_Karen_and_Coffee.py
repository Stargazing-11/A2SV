n, k, q = map(int, input().split())
recipes = []
for i in range(n):
    recipes.append(list(map(int, input().split())))

questions = []

for i in range(q):
    questions.append(list(map(int, input().split())))

ranges = [0 for _ in range(0,200000+1)]

for recipe in recipes:
    ranges[recipe[0]] += 1
    if recipe[1] + 1 < len(ranges):
        ranges[recipe[1] + 1] -= 1

for i in range(1, len(ranges)):
    ranges[i] += ranges[i-1]
count = [0 for _ in range(len(ranges)+1)]

for i in range(1, len(count)):
    if ranges[i-1] >= k:
        count[i] += count[i-1] + 1
    else:
        count[i] = count[i-1]
for ques in questions:
    print(count[ques[1] + 1] - count[ques[0]])
