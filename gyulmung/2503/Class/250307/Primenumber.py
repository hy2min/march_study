# prime number 소수 구하기
# 1과 자기 자신으로만 나눌 수 있는 수

# N 보다 작은 소수를 전부 출력하기
a = int(input()) # N 값 입력
ans = []
for i in range(2, a+1): # 2부터 N까지 확인
    Flag = 0
    for j in range(2, i): # 2부터 i보다 작은수로 나눠지는 확인할 수
        if i % j == 0: # 나눠 진다면
            Flag = 1 # 소수가 아님
            break
    if Flag == 0: ans.append(i) # break가 안걸린 친구들은 소수임!
print(ans)

b = int(input())
check = [0]*(a+1)
end = int(a**0.5)

for i in range(2, end + 1): # 1. 2부터 입력받은 수까지 확인
    if check[i] == 1: continue # 4. 이미 체크가 된  값이라면 pass
    for j in range(i+i, a+1, i): # 2. 작은 수부터 배수에 해당하는 인덱스에
        check[j] = 1             # 3. 1 체크하기

# 5. 소수 출력하기
for i in range(2, a+1):
    if check[i] == 0: print(i, end=' ')