"""PEP8"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c > 0:
    n = b*a
    m = (d//b)*c
    k = (d-((d//b)+b))*a

    print(n+m+k)
elif c == 0:
    n = d*a
    m = (d-b)//b
    print(n-m)
