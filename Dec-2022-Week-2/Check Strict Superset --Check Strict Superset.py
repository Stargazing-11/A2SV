# Enter your code here. Read input from STDIN. Print output to STDOUT

def superSet():

    a = set(input().split(" "))
    n = int(input())

    sets = []

    for i in range(n):
        input1 = set(input().split(" "))
        sets.append(input1)

    for set1 in sets:
        if a.issuperset(set1) and len(a) > len(set1):
            continue
        else:
            print(False)
            return 0
    print(True)


superSet()
