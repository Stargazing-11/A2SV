def swap_case(s):
    ans = []
    for i in s:
        if 65 <= ord(i) <= 90:
            ans.append(chr(ord(i) + 32))
        elif 97 <= ord(i) <= 122:
            ans.append(chr(ord(i) - 32))
        else:
            ans.append(i)
    return "".join(ans)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
