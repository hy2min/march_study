t = int(input())

for t in range(1,1+t) :
    forth = list(input().split()) # 리스트로 받고
    stack = [] # 스택 만들고
    error = False # 에러 확인용 플래그 만들고


    for i in range(len(forth) - 1 ) :
        if  forth[i].isdigit(): # 숫자면 스택에 추가
            stack.append(forth[i])

        else:
            try: # 숫자가 아니면 스택에서 숫자를 꺼내서 계산
                b =  int(stack.pop())
                a = int(stack.pop())

                if forth[i] == '+' : # 연산자에 맞춰서 연산
                    c = a+b
                elif forth[i] == '-':
                    c = a - b
                elif forth[i] == '*':
                    c = a * b
                elif forth[i] == '/':
                    c = a // b
                stack.append(c)
            except : # 예회발생시 에렃리
                error = True

    if error == True or len(stack) != 1 :
        print(f"#{t} error")
    else:
        print(f"#{t} {stack.pop()}")

        ## 왜안돼