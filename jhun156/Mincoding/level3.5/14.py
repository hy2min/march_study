a,b = map(int,input().split())

if a != 1111:
    print("아이디가 틀렸습니다")
elif a == 1111 and b != 2222:
    print("비밀번호가 틀렸습니다")
else:
    print("로그인성공")