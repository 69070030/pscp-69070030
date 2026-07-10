"""kkk"""
x = int(input())
y = int(input())

if x >= 1 and y >= 1:
    print("Q1")
elif x <= -1 and y <= -1:
    print("Q3")
elif x >= 1  and y <= -1:
    print("Q4")
elif x <= -1 and y >= 1:
    print("Q2")
elif not x and not y:
    print("O")
elif not x and y:
    print("Y")
elif not y and x:
    print("X")
