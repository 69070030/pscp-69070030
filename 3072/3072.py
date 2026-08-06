"""AEIOU"""
text = input().lower()
a = 0
e = 0
i = 0
o = 0
u = 0
for x in text:
    if x == "a":
        a += 1
    elif x == "e":
        e += 1
    elif x == "i":
        i += 1
    elif x == "o":
        o += 1
    elif x == "u":
        u += 1
if a > 0:
    print("a :", a)
if e > 0:
    print("e :", e)
if i > 0:
    print("i :", i)
if o > 0:
    print("o :", o)
if u > 0:
    print("u :", u)
