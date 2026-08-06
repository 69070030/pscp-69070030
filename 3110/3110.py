"""สงครามส่งด่วน"""
start, end = input().split()
weight = float(input())
price = 0
if start == "BKK" and end == "CNX":
    price = 10 + weight * 30
elif start == "CNX" and end == "UBP":
    price = 15 + weight * 40
elif start == "UBP" and end == "BKK":
    price = 20 + weight * 40
elif start == "BKK" and end == "PKT":
    price = 25 + weight * 50
elif start == "PKT" and end == "CNX":
    price = 30 + weight * 60
elif start == "UBP" and end == "PKT":
    price = 40 + weight * 70
else:
    price = "Error"
if price == "Error":
    print(price)
else:
    print(f"{price:.2f}")
