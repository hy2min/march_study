T = 10
for idx in range(10):
    ans = 0
    n = int(input())
    str = input()
    # 중위 > 후위표기식으로 변환
    # 1. result 라는 변수에 숫자는 그냥 저장
    # 2. 연산자라면 스택이 비어있으면 그냥 넣고 비어있지 않으면 pop한 값 result 에 추가 후에 연산자 push
    # 3. 마지막으로 스택에 남은 연산자들은 모두 result로 옮기기
    result = ""
    stack = []
    for i in str:
        if i.isdigit(): # 숫자인 경우
            result += i
        else: # 연산자인 경우
            if stack: # 스택이 비어있지 않다면(True)
                result += stack.pop() # pop해서 result 에 추가
                stack.append(i) # 새로 저장할 연산자를 push
            else: # 스택이 비어있다면
                stack.append(i)


    result += stack.pop()

    # 연산자가 +만 있는 경우에는 무조건 stack에 1개만 남아서 while문이나 for문을 돌릴 필요가 없지만, 만약 있다면 반복문 필요

    # 후위표기식을 계산해서 출력하기
    # 1. 숫자는 그냥 stack에 push
    # 2. 연산자는 stack에서 2개 pop한 다음 연산하고 넣기
    # 3. 마지막에 남아있는 게 정답

    for i in result:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
    ans = stack.pop()

    print(f'#{idx + 1} {ans}')