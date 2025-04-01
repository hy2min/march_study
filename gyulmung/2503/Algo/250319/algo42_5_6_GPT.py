import sys
sys.stdin = open('input.txt', 'r')


# copy.deepcopy를 사용하지 않음
arr = list(input())
n = int(input())
length = len(arr)
Max = -1e8

# 조건에 맞는 점수를 계산하는 함수
def calculate_score():
    Sum = 0
    for i in range(length - 1):
        if arr[i] == arr[i + 1]:  # 이웃한 글자가 같을 때
            Sum -= 50
        elif abs(ord(arr[i]) - ord(arr[i + 1])) <= 5:  # 차이가 5 이하일 때
            Sum += 3
        elif abs(ord(arr[i]) - ord(arr[i + 1])) >= 20:  # 차이가 20 이상일 때
            Sum += 10
    return Sum

# n번의 교환을 시도하며 최대 점수 구하기
def change(lev):
    global Max
    if lev == n:
        score = calculate_score()
        Max = max(Max, score)
        return

    for i in range(length):
        for j in range(i + 1, length):  # i와 j를 바꿀 때 j > i로만 제한
            arr[i], arr[j] = arr[j], arr[i]  # 두 원소를 교환
            change(lev + 1)  # 한 번의 교환을 마친 후 다음 교환
            arr[i], arr[j] = arr[j], arr[i]  # 다시 원래 상태로 복구

change(0)
print(Max)
