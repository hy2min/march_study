arr = [
    ['A', '7', '9', 'T', 'K', 'Q'],
    ['M', 'I', 'N', 'C', 'O', 'D']
]


a,b = map(str,input().split())

for i in range(2) :
    if a in arr[i] :
        print(f"{a} : 존재")
        break
else :
        print(f"{a} : 없음")

for i in range(2) :
    if b in arr[i] :
        print(f"{b} : 존재")
        break
else :
        print(f"{b} : 없음")