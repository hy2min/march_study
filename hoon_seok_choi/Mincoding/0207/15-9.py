a = "BBQWORLD"
b = "KFCAPPLE"
c = "LOT"

arr =[*a,*b,*c]
cnt=0

d = input()

for i in arr :
    if i == d :
        cnt+=1

print(cnt)