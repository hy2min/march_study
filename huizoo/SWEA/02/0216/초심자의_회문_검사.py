t = int(input())
for tc in range(1, t+1):
    st = input()
    if st == st[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')