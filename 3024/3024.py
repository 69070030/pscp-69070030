"""SurprisingVote"""
total = float(input())
highest = float(input())
min = max(0.0 , total - (2*highest))
if highest - min > 2:
    print("Surprising")
else:
    print("Not surprising")
