"""2996"""
Word = str(input()).lower()[:5]
ans = ""
for i in range (len(Word)):
    ans += Word[-i - 1]
print(ans)
