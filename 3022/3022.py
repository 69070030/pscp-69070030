"""Temp"""
tem = float(input())
nuay1 = str(input())
nuay2 = str(input())
if nuay1 =="C":
    cel = tem
elif nuay1 =="K":
    cel = tem - 273.15
elif nuay1 =="F":
    cel =((tem-32)*5)/9
elif nuay1 =="R":
    cel = tem*5/9 - 273.15
if nuay2 == "C":
    print(f"{cel:.2f}")
elif nuay2 == "K":
    print(f"{cel+273.15:.2f}")
elif nuay2 == "R":
    print(f"{(cel+273.15)*9/5:.2f}")
elif nuay2 == "F":
    print(f"{cel*9/5+32:.2f}")
