import sys
sys.stdin = open('input.txt','r')

T = 10
for test in range(1, T+1):
    N = int(input())
    arr = input()
    # 전위를 후위로 바꾸기
    plus_multi = {'+': 1, '*': 2}
    result = ''
    q = []
    for i in arr:
        if i.isdigit():
            result += i
        else:
            if q and plus_multi[i] <= plus_multi[q[-1]]:
                result += (q.pop())
            q.append(i)
    while q:
        result += q.pop()

    # 후위식 계산
    for i in result:
        if i.isdigit():
            q.append(int(i))
        else:
            a = q.pop()
            b = q.pop()
            if i == '+':
                q.append(a+b)
            elif i == '*':
                q.append(a*b)
    ans = q.pop()
    print(f'#{test} {ans}')