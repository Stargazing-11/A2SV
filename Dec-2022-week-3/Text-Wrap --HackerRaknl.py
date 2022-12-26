import textwrap


def wrap(string, max_width):
    ans = ""
    for index, s in enumerate(string):
        ans += s
        if (index + 1) % max_width == 0:
            ans += "\n"
    return ans


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
