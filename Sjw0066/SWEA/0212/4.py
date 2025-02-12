T=int(input())
for tc in range(1,T+1):
    str1=input()
    if str1 == str1[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')