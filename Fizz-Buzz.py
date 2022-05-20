def fizz(n):
    x = []
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            x.append("FizzBuzz")
        elif i%3 ==0 and i%5!=0:
            x.append("Fizz")
        elif i%3!=0 and i%5==0:
            x.append("Buzz")
        else:
            x.append(str(i))
    return x

print(fizz(5))