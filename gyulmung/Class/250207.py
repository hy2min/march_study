# Direct Address Table
# 1. 장점 - 빠른 검색
# 2. 단점 - 입력데이터에 따라 비효율적인 메모리 사용
#         - 검색을 하기 위해선 정수값이어야한다.
import sys
sys.stdin = open('input.txt','r')

# n = int(input())
# arr = list(map(int, input().split()))
# lst = [0]*10
#
# for i in range(n):
#     lst[arr[i]] += 1
#
# for i in range(len(lst)):
#     if lst[i] != 0:
#         print(f'{i} : {lst[i]}개 있음')

# 어떤 알파벳이 몇개씩 사용되었는지 출력하기기
# banana
lst = list(input())
print(lst)
arr = [0]*100

for i in range(6):
    arr[ord(lst[i])] += 1

for i in range(len(arr)):
    if arr != 0:
        print(f'{arr} : {arr[i]}개 있음')