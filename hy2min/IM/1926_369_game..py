N = int(input())

for i in range(1, N+1):
    cnt = 0
    for num in str(i):
        cnt += num.count("3")
        cnt += num.count("6")
        cnt += num.count("9")
    if cnt != 0:
        print('-'*cnt, end=" ")
    else:
        print(i, end=" ")
