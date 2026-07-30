"""Goal"""
a = int(input())
b = int(input())
goal = int(input())
B = b*5
if goal-B < a and goal-B > 0:
    print(goal-B)
elif goal-B >a or goal%5 > a:
    print(-1)
elif goal%5 < a:
    print(goal%5)
