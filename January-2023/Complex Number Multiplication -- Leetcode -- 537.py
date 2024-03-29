class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")

        real = ((int(num1[1][:-1]) * int(num2[1][:-1]))
                * - 1) + int(num1[0]) * int(num2[0])
        imaginary = (int(num1[0]) * int(num2[1][:-1])) + \
            (int(num2[0]) * int(num1[1][:-1]))
        ans = str(real) + "+" + str(imaginary) + "i"
        return ans
