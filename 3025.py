"""Season"""
mon = int(input())
day = int(input())
if (mon == 12 and day >= 21) or mon in (1,2) or (mon == 3 and day < 21):
    print("winter")
elif (mon == 3 and day >= 21) or mon in (4,5) or (mon == 6 and day < 21):
    print("spring")
elif (mon == 6 and day >= 21) or mon in (7,8) or (mon == 9 and day < 21):
    print("summer")
elif (mon == 9 and day >= 21) or mon in (10,11) or (mon == 12 and day < 21):
    print("fall")
