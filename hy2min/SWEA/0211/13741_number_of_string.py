T = int(input())
for idx in range(T):
    str1 = input()
    str2 = input()
    arr = [0] * len(str1)
    for i in range(len(str1)):
        for j in str2:
            if str1[i] == j:
                arr[i] += 1

    print(f'#{idx+1} {max(arr)}')


