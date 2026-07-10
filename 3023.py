n = int(input())

if n == 1:
    print(1)
else:
    digit_press = 0
    for i in range(1, n + 1):
        digit_press += len(str(i))
    print(digit_press + n)