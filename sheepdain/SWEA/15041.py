T = int(input())
for test_case in range(1, T + 1):
    arr = list(input().split())
    result = []
    try:
        for i in arr:
            if i == '.':
                if len(result) == 1:
                    print(f'#{test_case}', result.pop())
                else:
                    print(f'#{test_case} error')
            elif i.isdigit():
                result.append(int(i))
            else:
                b, a = result.pop(), result.pop()
                if i == '+':
                    result.append(a + b)
                elif i == '-':
                    result.append(a - b)
                elif i == '*':
                    result.append(a * b)
                elif i == '/':
                    result.append(a // b)
    except:
        print(f'#{test_case} error')
