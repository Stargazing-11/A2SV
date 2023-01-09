# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for cases in range(t):
    size = int(input())
    blocks = list(map(int, input().split()))
    output = 'Yes'

    while len(blocks) > 1:
        if blocks[-1] >= blocks[0]:
            large = blocks[-1]
            blocks.pop()
        else:
            large = blocks[0]
            blocks.pop(0)

        if blocks[0] > large or blocks[-1] > large:
            output = 'No'
            break
    print(output)
