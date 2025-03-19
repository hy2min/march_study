import sys

sys.stdin = open("input.txt", "r")

ratio = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4, (2, 3, 1): 5,
         (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}  # 맨앞 0을 제외한 2번,3번,4번 칸의 비율

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    code = list(set([input() for _ in range(N)]))  # 겹치는 줄 지워버리자
    answer = 0  # 최종 결과 값
    temps = []  # 임시로 저장해줘야하는 값
    for i in code:  # 코드 내용물들
        result = format(int(i, 16), 'b').lstrip('0')  # 16진법을 2진법으로 바꿔주자
        n1 = n2 = n3 = 0  # 비율 계산
        cnt = 0
        even = odd = 0  # 홀짝
        overlap = ''  # 겹쳐지는 녀석
        for j in result:  # 리스트 내용물에서
            if j == '1' and n2 == 0:  # 1을 받았는데 n2=0이면
                n1 += 1  # n1에 1 더해
            elif j == '0' and n1 != 0 and n3 == 0:  # 0을 받았는데 n1의 값이 0이 아니고 n3의 값이 0이면
                n2 += 1  # n2에 1 더해
            elif j == '1' and n2 != 0:  # 다시 1을 받았는데 n2가 0이 아니면(n3이란 뜻)
                n3 += 1  # n3에 1 더해
            elif n3 != 0:  # 위케이스 다 지났는데 n3가 0이 아니면 -> 즉 코드를 받았다면
                cnt += 1  # 횟수 증가
                r = min(n1, n2, n3)  # 비율 나눠줘야 하니까 최소값을 구해서
                nums = ratio[(n1 // r, n2 // r, n3 // r)]  # 최소 값으로 나눠 비율을 맞춰주자
                overlap += str(nums)  # 이 때의 코드 번호 저장하자
                if cnt == 8:  # 암호가 8자리가 됐다면
                    if (odd * 3 + even + nums) % 10 == 0 and overlap not in temps:  # 조건에 맞고, 겹치는 놈이 없으면
                        answer += odd + even + nums  # 답에 지금 암호값 더하자
                    temps.append(overlap)  # 나중에 겹치는놈 체크용
                    even = odd = 0  # 홀수 짝수 초기화
                    cnt = 0  # 횟수도 초기화
                    overlap = ''  # 암호도 초기화
                elif cnt % 2 == 0:  # 8자리가 아니라면, 홀수 값을 모아주자
                    even += nums
                else:
                    odd += nums  # 짝수 값을 모아주자
                n1 = n2 = n3 = 0  # 비율도 초기화
    print(f'#{case} {answer}')