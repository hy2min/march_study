def abc():
    global cnt, overlap, even, odd, ans
    cnt += 1  # 횟수 증가
    r = min(a, b, c)  # 비율 나눠줘야 하니까 최소값을 구해서
    num = PASSWORD[(a // r, b // r, c // r)]  # 최소 값으로 나눠 비율을 맞춰주자
    overlap += str(num)  # 이 때의 코드 번호 저장하자
    if cnt == 8:  # 암호가 8자리가 됐다면
        if (odd * 3 + even + num) % 10 == 0 and overlap not in checked:  # 조건에 맞고, 겹치는 놈이 없으면
            ans += odd + even + num  # 답에 지금 암호값 더하자
        checked.append(overlap)  # 나중에 겹치는놈 체크용
        even = odd = 0  # 홀수 짝수 초기화
        cnt = 0  # 횟수도 초기화
        overlap = ''  # 암호도 초기화
    elif cnt % 2 == 0:  # 8자리가 아니라면, 홀수 값을 모아주자
        even += num
    else:
        odd += num  # 짝수 값을 모아주자


PASSWORD = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
            (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}  # 맨앞 0을 제외한 2번,3번,4번 칸의 비율

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(set([input() for _ in range(N)]))  # 겹치는 줄 지워버리자
    ans = 0  # 최종 결과 값
    checked = []  # 임시로 저장해줘야하는 값
    for row in arr:  # 코드 내용물들
        num = format(int(row, 16), 'b').strip('0')  # 16진법을 2진법으로 바꿔주자
        a = b = c = 0  # 비율 계산
        cnt = 0
        even = odd = 0  # 홀짝
        overlap = ''  # 겹쳐지는 녀석
        for i in num:  # 리스트 내용물에서
            if i == '1' and b == 0:  # 1을 받았는데 b=0이면
                a += 1  # a에 1 더해
            elif i == '0' and a != 0 and c == 0:  # 0을 받았는데 a의 값이 0이 아니고 c의 값이 0이면
                b += 1  # b에 1 더해
            elif i == '1' and b != 0:  # 다시 1을 받았는데 b가 0이 아니면(c이란 뜻)
                c += 1  # c에 1 더해
            elif c != 0:  # 위케이스 다 지났는데 c가 0이 아니면 -> 즉 코드를 받았다면
                abc()
                a = b = c = 0  # 비율 초기화
        if c != 0:
            abc()
    print(f'#{tc} {ans}')