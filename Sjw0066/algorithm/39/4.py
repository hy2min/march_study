money=int(input())
coin=[10,50,100,500]
coin.sort(reverse=True)

cnt=0
for i in range(4):
    cnt += money // coin[i]
    money%=coin[i]


print(cnt)
