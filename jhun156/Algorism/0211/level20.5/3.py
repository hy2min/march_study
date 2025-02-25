string = input()
n = len(string)
num = n//2
if string[:num] == string[num:]:
    print("동일한문장")
else:
    print("다른문장")