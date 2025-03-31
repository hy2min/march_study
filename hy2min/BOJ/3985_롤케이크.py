l = int(input())
n = int(input())
arr = [0] *l
expect_m = 0
for num in range(1,n+1):
    p, k = map(int,input().split())
    p -= 1
    k -= 1

    if k-p > expect_m:
        expect_m = k-p
        expect_p = num
    for i in range(p,k+1):
        if arr[i] == 0:
            arr[i] = num
real_m = 0
for i in range(1, n+1):
    if arr.count(i) > real_m:
        real_m = arr.count(i)
        real_p = i

print(expect_p)
print(real_p)

