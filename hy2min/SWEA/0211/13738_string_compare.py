T = int(input())
for idx in range(T):
    str1 = input()
    str2 = input()
    n = len(str1)
    m = len(str2)
    answer = 0
    for i in range(m-n+1):
        if str1 == str2[i:i+n]:
                answer = 1
                break
    print(f'#{idx+1} {answer}')

