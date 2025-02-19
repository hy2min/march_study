s = input()
n = len(s)//2
if s[:n] == s[n:]:
    print("동일한문장")
else:
    print("다른문장")