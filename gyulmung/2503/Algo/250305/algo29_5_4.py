arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.append(101)
arr2.append(101)
cnt1, cnt2 = 0, 0
ret = []

while 1:
    if cnt1 == 4 and cnt2 == 4: break
    if arr1[cnt1] >= arr2[cnt2]:
        ret.append(arr2[cnt2])
        cnt2+=1
    else:
        ret.append(arr1[cnt1])
        cnt1+=1

print(*ret)