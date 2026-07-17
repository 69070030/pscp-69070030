"""Bill"""
price = int(input())
a = price/10
if a > 1000:
    a = 1000
if a < 50:
    a = 50
price = price + a
price = price*1.07
print(f"{price:.2f}")
