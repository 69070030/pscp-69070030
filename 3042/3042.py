"""หารลงตัว10"""
N = int(input())
while N >= 0:
    if N % 10 == 0:
        print(N, end=" ")
    N -= 1
